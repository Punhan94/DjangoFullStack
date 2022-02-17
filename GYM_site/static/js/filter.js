const filter = document.getElementById('filter');
const hidefilter = document.getElementById('dropdownhide-shopping');
const category = document.getElementById('category');
const hidecategory = document.getElementById('dropdownhide-category');


function elave(x, y) {
    x.addEventListener('click', function () {
        y.classList.toggle('shopping-views')
    });
};

elave(filter, hidefilter);
elave(category, hidecategory);

    
