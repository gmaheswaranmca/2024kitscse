let first = {name:'dravid',sal:20000}, 
    second={name:'ganguli',sal:30000}, 
    third={name:'dhoni',sal:25000};
// find second max of three salaries 

let max;
if(first.sal > second.sal && 
    first.sal > third.sal){
    max = first;
}else if(second.sal > third.sal) {
    max = second;
}else {
    max = third;
}

let min;
if(first.sal < second.sal && 
        first < third){
    min = first;
}else if(second.sal < 
        third.sal) {
    min = second;
}else {
    min = third;
}

let smax = (first.sal + 
        second.sal + 
        third.sal) 
        - max.sal 
        - min.sal;
console.log(smax)