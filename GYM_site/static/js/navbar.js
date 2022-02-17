// const navbar = document.getElementById('navbar');
// const kecidlerA = document.getElementsByClassName('kecidler-a');


// for (let i = 0; i < kecidlerA.length; i++) {
//     kecidlerA[i].addEventListener("click", function x () {
//         var current = document.getElementsByClassName("active-kecidler-a");
//         if (current.length > 0) {
//            return current[0].classList.remove("active-kecidler-a");
//         }
//          return this.classList.add('active-kecidler-a');
//     })
// };
// if (window.onload) {
//   x()
// }


const search = document.getElementById('search');
const hidesearch = document.getElementById('hide-search');

function elave(x, y) {
  x.addEventListener('click', function () {
      y.classList.toggle('shopping-views')
  });
};

elave(search, hidesearch);