import uuid

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from DjangoProjectexposer.models import Client, Marchandise, Paiement


def paiements_invalides(request):
    invalid_paiements = Paiement.objects.filter(est_valide=False).order_by('-date_paiement')
    return render(request, 'paiement/li_paiements_invalides.html', {'invalid_paiements': invalid_paiements})


def liste_paiements(request):
    paiements = Paiement.objects.select_related('client').all().order_by('-date_paiement')
    return render(request, 'paiement/li_payements.html', {'paiements': paiements})


def enregister_paiement(request):
    if request.method == 'POST':
        try:
            client_id = request.POST['client']
            client = Client.objects.get(id_client=client_id)  # Corrected: Fetch client by ID
            marchandises_data = request.POST.getlist('marchandise')
            montant_total = request.POST['montant_total']

            # Process selected merchandise items and prepare JSON data
            marchandises = []
            for marchandise_id in marchandises_data:
                marchandise = Marchandise.objects.get(numero_marchandise=marchandise_id)  # Fetch marchandise object
                marchandises.append({
                    'numero_marchandise': marchandise.numero_marchandise,
                    'nom': marchandise.nom,
                    'description': marchandise.description,
                    'prix': marchandise.prix
                })

            paiement = Paiement(
                est_valide=True,
                client=client,
                marchandises=marchandises,  # Save as JSON
                montant_total=montant_total,
                date_paiement=timezone.now(),
                token=uuid.uuid4()
            )
            paiement.save()

            return render(request, 'paiement/enregistrer_paiement.html', {
                'clients': Client.objects.all(),
                'marchandises': Marchandise.objects.all(),
                'success_message': "Le paiement a été enregistré avec succès !",  # Success message
                'show_banner': True  # Show banner for 5 seconds
            })

        except Exception as e:
            print(f"Error during payment processing: {e}")
            return render(request, 'paiement/enregistrer_paiement.html', {  # Render error on same page
                'clients': Client.objects.all(),
                'marchandises': Marchandise.objects.all(),
                'error_message': f"Une erreur est survenue : {e}"  # Display specific error message
            })

    clients = Client.objects.all()
    marchandises = Marchandise.objects.all()
    return render(request, 'paiement/enregistrer_paiement.html', {'clients': clients, 'marchandises': marchandises})


def supprimer_paiement(request, id_paiement):
    paiement = get_object_or_404(Paiement, numero_paiement=id_paiement)
    if request.method == 'POST':
        # Vérifie si le bouton "supprimer" a été activé
        if "supprimer" in request.POST:
            paiement.delete()
            return redirect('listePaiements')
            # Affiche une page de confirmation pour la suppression
    return render(request, 'paiement/supprimer_paiement.html', {'details': paiement})
