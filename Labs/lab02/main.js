function calculate() {
    var str = document.getElementById("input");
    try {
        eval(str.value);
        console.log(isFinite(eval(str.value))) 
        if (!isFinite(eval(str.value)))
        {
            alert("Division by Zero!");
            //document.getElementById("result").innerHTML = "Error";
            return
        }
    } 
    catch (e) {

       alert("You must enter numbers");
    
    }
    //document.getElementById("result").innerHTML = eval(str.value);
    str.value = str.value + " \= " + eval(str.value);
    document.getElementById("input").focus()
    
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

function sqrt() {
    var orig = document.getElementById("input");
    try {
        if (eval(orig.value) < 0){
            alert("Cannot take a square root");
        }
        else{
            orig.value = Math.sqrt(eval(orig.value))
            document.getElementById("input").focus() 
        }
    }

    catch (e){

        alert("Cannot take a square root");
    }
}

function power() {
    var orig = document.getElementById("input");
    var array = orig.value.split("power")
    console.log(array)
    try {
            var res = Math.pow(eval(array[0]),eval(array[1]))
            
            orig.value = res
            document.getElementById("input").focus() 
        
    }

    catch (e){

        alert("Cannot Exponentiate");
    }
  }