let counter = 0;
// creates a variable
function count(){
    counter ++;
    document.querySelector('h1').innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`Counter is ${counter}`)
        // ` ` acts as the f'' in python ${} is used for {} in python
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
    // this line will assign the counter function to the onclick property of the button    
});
// DOMcontentloaded runs the script only after the whole document is loaded