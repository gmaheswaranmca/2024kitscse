// let and const 
/*
// value variables 
let first = 10
first = 20
console.log(first)

const second=30
second=40           //ERR "Assignment to constant variable"
console.log(second)
*/
//ref variables
/*
let susmitha = {rollnumber: '577', name: 'susmitha'}
susmitha = {rollnumber: '570', name: 'susmitha'}

const sohail = {rollnumber: '5H1', name: 'sohail'}
sohail = {rollnumber: '5H2', name: 'sohail'}
*/


let susmitha = {rollnumber: '577', name: 'susmitha'}
susmitha.rollnumber = '570'
console.log(susmitha)
const sohail = {rollnumber: '5H1', name: 'sohail'}
sohail.rollnumber = '5H2'
console.log(sohail)