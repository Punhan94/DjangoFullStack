const dropdownMobile = document.getElementById("dropdown-mobile");
const dropdownhideMobile = document.getElementById("dropdownhide-mobile");

dropdownMobile.addEventListener('click', function () {
    dropdownhideMobile.classList.toggle("dropdown-mobile-toggle")
});