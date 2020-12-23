let vats = document.getElementById("vats");


// window.time = 0; //global declaration
// function autorefresh() {
//     var isChecked = document.getElementById("vats").checked;
//     if (isChecked == true) {
//         time = setInterval(function() {
//             alert('hello');
//             isChecked == true;
//         }, 3000);
//     } else if (isChecked == false) {
//         clearInterval(time);
//     }
// }
// autorefresh();
// document.getElementById('vats').addEventListener('click', autorefresh);

vats.addEventListener("change", function write() {
    if (vats.checked == true) {
        time = setInterval(() => {
            let vats = document.getElementById("vats");
            vats.checked = "false";

            console.log("hy");
        }, 3000);
    } else if (vats.checked == false) {
        clearInterval(time);
    }
    setInterval(() => {
        vats.checked == false;
        console.log("hello");
    }, 3000);

});