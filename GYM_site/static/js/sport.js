const femaleradion = document.getElementById('female');
const maleradion = document.getElementById('male');
const sportBody = document.getElementsByClassName('sports-body');


function radioFunction(x) {
    x.addEventListener('change',function(){
        if (x == femaleradion) {
            sportBody[0].classList.add('sport-hidden');
            sportBody[1].classList.remove('sport-hidden')
            console.log('isledi')
        }
        else {
            sportBody[1].classList.add('sport-hidden');
            sportBody[0].classList.remove('sport-hidden')
            console.log('islediii')
        }
    })
}
radioFunction(maleradion)
radioFunction(femaleradion)