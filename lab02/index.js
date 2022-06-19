console.log("Hello world")
var number = 5; // in-line comment
/*
block comment
*/
//WITHOUT var all variables become global
var Name = "Mik";
alert(Name)

//console.log(Name);

Name = 6;

//console.log(Name);

Name = Name + 4;

//console.log(Name);

let hisName = "Tim";
const herName = "Shouq";

var str = " this is the qoute \" "

//console.log(str);

//Concat strings

//console.log(Name + str)

//length of a string

//console.log(str.length)

//console.log(str[1])

//Strings are immutable

//functions
function foo(x){
    var answ = "The answer is: " + x
    return answ
}
console.log(foo(5))

//append

var array = [2, "some string"]
array.push(3)

console.log(array)

//remove last element
array.pop()
console.log(array)

//remove first element
array.shift()
console.log(array)

//add first element
array.unshift('first')
console.log(array)

