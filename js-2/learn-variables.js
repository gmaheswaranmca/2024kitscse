// var, let, const 
/*
var first = 10;

function f() {
    first = 20;
}

f();
console.log(first)
*/
function g() {
    let second = 30;
    {
        console.log(second);
        let third = 40;
    }
    console.log(second, third) //ERR "third" is not defined in the scope
}
g()