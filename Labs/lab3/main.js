function changeKg(kg) {
    var pounds = document.getElementById('pounds');
    pounds.value = kg.value * 2.205;
}

function changePounds(pounds) {
    var kg = document.getElementById('kg');
    kg.value = pounds.value * 0.4535 ;
}

function changeKm(km) {
    var miles = document.getElementById('miles');
    miles.value = km.value *  0.621371;
}

function changeMiles(miles) {
    var km = document.getElementById('km');
    km.value = miles.value * 1.60934;
}

function changeCelsius(cel) {
    var fah = document.getElementById('fahrenheit');
    fah.value = (cel.value * 9/5) + 32;
}

function changeFahrenheit(fah) {
    var cel = document.getElementById('celsius');
    cel.value = (fah.value - 32) * 5/9;
}