let fn = document.getElementById("id_expertiseFunction");
let yr = document.getElementById("yearsInterviewed");

document.onreadystatechange=function(){
//all onload actions
    fn.classList.add("ex-input");
    fn.style.color ='#d2d2d2';
    yr.style.color = '#d2d2d2';
}

fn.onchange = function colorChange() {
    var value = fn.options[fn.selectedIndex].value;
    if (value == "")
        fn.style.color = '#d2d2d2';
    else
        fn.style.color = '#222222';
}

yr.onchange = function colorChange() {
    console.log("changed")
    var value_yr = yr.options[yr.selectedIndex].value;
    if (value_yr == "")
        yr.style.color = '#d2d2d2';
    else
        yr.style.color = '#222222';
}
