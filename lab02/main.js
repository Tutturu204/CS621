function calculate() {
    var str = document.getElementById("input").value;
    try {
        eval(str);
        console.log(isFinite(eval(str))) 
        if (!isFinite(str))
        {
            alert("Division by Zero!");
            document.getElementById("result").innerHTML = "Error";
            return
        }
    } 
    catch (e) {

       alert("You must enter numbers");
    
    }
    document.getElementById("result").innerHTML = eval(str);
  }

function add() {
    var orig = document.getElementById("input");
    orig.value = orig.value + "+";
    document.getElementById("input").focus()
}

function sub() {
    var orig = document.getElementById("input");
    orig.value = orig.value + "-";
    document.getElementById("input").focus()
}

function mult() {
    var orig = document.getElementById("input");
    orig.value = orig.value + "*";
    document.getElementById("input").focus()
}

function div() {
    var orig = document.getElementById("input");
    orig.value = orig.value + "/";
    document.getElementById("input").focus()
}