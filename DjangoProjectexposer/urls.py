"""
URL configuration for DjangoProjectexposer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import Mapping
import paiement.views
from DjangoProjectexposer import settings
from Mapping import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('login/', views.create_user),
    path('form/', views.form, name='form'),
    path('map/', views.map),
    path('client/', views.client, name='list_client'),
    path('client/<int:id_client>/', Mapping.views.client_details, name='client'),
    path('adresse/<int:id_client>/', Mapping.views.Adresse_Choice, name='ajouter_adresse'),
    path('client/delete/<int:id_client>/', Mapping.views.supprimer_client, name='supprimer_client'),
    path('client/modifier/<int:id_client>/', Mapping.views.modifier_client, name='modifier_client'),

    # path('paiement/', include('paiement.urls')),

    path('paiement/enregistrer/', paiement.views.enregister_paiement, name='enregistrer_paiement'),
    path('paiement/liste/', paiement.views.liste_paiements, name='listePaiements'),
    path('paiement/invalides/', paiement.views.paiements_invalides, name='paiementsInvalides'),

    path('paiement/delete/<int:id_paiement>/', paiement.views.supprimer_paiement, name='supprimer_paiement'),

]

if settings.DEBUG:  # Servir les fichiers médias seulement en développement
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
