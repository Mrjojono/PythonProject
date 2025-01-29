var naLink = document.getElementById("n-a");
var saLink = document.getElementById("s-a");
var eurLink = document.getElementById("eur");
var afrLink = document.getElementById("afr");
var asiLink = document.getElementById("asi");
var ausLink = document.getElementById("aus");
var naAbout = document.getElementById("north-america");
var saAbout = document.getElementById("south-america");
var eurAbout = document.getElementById("europe");
var afrAbout = document.getElementById("africa");
var asiAbout = document.getElementById("asia");
var ausAbout = document.getElementById("australia");

var link = [naLink, saLink, eurLink, afrLink, asiLink, ausLink];

var about = [naAbout, saAbout, eurAbout, afrAbout, asiAbout, ausAbout];


link[0].addEventListener("mouseover", (e) => {
    about[0].style.display = "block";
});
link[0].addEventListener("mouseleave", (e) => {
    about[0].style.display = "none";
});
link[1].addEventListener("mouseover", (e) => {
    about[1].style.display = "block";
});
link[1].addEventListener("mouseleave", (e) => {
    about[1].style.display = "none";
});
link[2].addEventListener("mouseover", (e) => {
    about[2].style.display = "block";
});
link[2].addEventListener("mouseleave", (e) => {
    about[2].style.display = "none";
});
link[3].addEventListener("mouseover", (e) => {
    about[3].style.display = "block";
});
link[3].addEventListener("mouseleave", (e) => {
    about[3].style.display = "none";
});
link[4].addEventListener("mouseover", (e) => {
    about[4].style.display = "block";
});
link[4].addEventListener("mouseleave", (e) => {
    about[4].style.display = "none";
});
link[5].addEventListener("mouseover", (e) => {
    about[5].style.display = "block";
});
link[5].addEventListener("mouseleave", (e) => {
    about[5].style.display = "none";
});