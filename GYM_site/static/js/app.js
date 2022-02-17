const woman = document.getElementById('vki-woman');
const man = document.getElementById('vki-man');
const gender = document.getElementById("vki-gender");


woman.addEventListener('click', function () {
woman.classList.add('active');
    man.classList.remove('active');
    gender.value = "woman";
});
man.addEventListener('click', function () {
    man.classList.add('active');
    woman.classList.remove('active');
    gender.value = 'man';
});

var slider1 = document.getElementById("height");
var output1 = document.getElementById("heightspan");
output1.innerHTML = slider1.value;
slider1.oninput = function () {
    output1.innerHTML = this.value;
};

var slider2 = document.getElementById("weight");
var output2 = document.getElementById("weightspan");
output2.innerHTML = slider2.value; 
slider2.oninput = function () {
    output2.innerHTML = this.value;
};


function vkiHesabla() {
    var kilo = document.getElementById("weightspan").innerText;
    var boy = document.getElementById("heightspan").innerText;
    if (gender.value == "man") {
        let VKI = eval(kilo / ((boy / 100) ** 2));
        let IVA = eval(50 + 2.3 * (((boy / 0.0254) / 100) - 60));
        let YVA = eval((1.10 * kilo) - 128*((kilo**2)/((100 * (boy/100))**2)));
        document.getElementById("VKI").innerText = VKI.toFixed(1);
        document.getElementById("VKI-yoxla").innerText = yoxla(VKI);
        document.getElementById("IVA").innerText = Math.round(IVA);
        document.getElementById("YVA").innerText = YVA.toFixed(1);
        document.getElementById("cavablar").classList.remove('hidden');
    }
    else if (gender.value == 'woman') {
        let VKI = eval(kilo / ((boy / 100) ** 2));
        let IVA = eval(45.5 + 2.3 * (((boy / 0.0254) / 100) - 60));
        let YVA = eval((1.07 * kilo) - 148*((kilo**2)/((100 * (boy/100))**2)));
        document.getElementById("VKI").innerText = VKI.toFixed(1);
        document.getElementById("VKI-yoxla").innerText = yoxla(VKI);
        document.getElementById("IVA").innerText = Math.round(IVA);
        document.getElementById("YVA").innerText = YVA.toFixed(1);
        document.getElementById("cavablar").classList.remove('hidden');
    }
};


function yoxla(x) {
    console.log(x)
    if (x < 18.49) {
        return 'İdeal Kilonun Altı'
    }
    else if (24.99 > x) {
        return 'İdeal Kiloya Sahibsiniz'
    }
    else if (29.99 > x) {
        return 'İdeal Kilonun Üstü'
    }
    else if(x>30) {
        return 'İdeal Kilonun Çox Üstü'
    }
};

