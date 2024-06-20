var number_list = [];
function doAdd(){
    let number = parseInt(document.getElementById('number').value);
    number_list.push(number);
    let items = '';
    for(let n of number_list) {
        items = items + `<LI>${n}</LI>`
    }
    let numbers_html = `<UL>${items}</UL>`
    document.getElementById("numbers-list").innerHTML = numbers_html;
}