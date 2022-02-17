const burgermenu = document.getElementById('hamburger');
const mobilemenu = document.getElementById('mobile-menu');

burgermenu.addEventListener('click', function () {
    mobilemenu.classList.toggle('mobile-menu-toggle');
});