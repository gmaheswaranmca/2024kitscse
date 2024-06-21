let first = 10, second=30, third=20;
// find second max of three numbers 

let max;
if(first > second && first > third){
    max = first;
}else if(second > third) {
    max = second;
}else {
    max = third;
}





let min;
if(first < second && 
        first < third){
    min = first;
}else if(second < third) {
    min = second;
}else {
    min = third;
}

let smax = (first + second + 
        third) - max - min;
console.log(smax)