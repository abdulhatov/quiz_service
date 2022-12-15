// document.addEventListener('readystatechange', event => {
//     myFunction(event);
// });
// function myFunction(){
//     let data = []
//
//     let checked_count = 0
//     var val = document.getElementsByClassName('field-correct')
//
//     for (x = 0; x < val.length-1; x++){
//             valu = document.getElementById('id_answer-'+x+'-correct');
//             console.log(valu)
//             data.push(valu)
//             if(data[x].checked == true){
//                 checked_count++;
//             }
//             valu.onclick = function () { myFunction(this) }
//         }
//         if (checked_count == val.length-2){
//             disable_check(data)
//         }
//         if (checked_count < val.length-2){
//             enable_check(data)
//         }
//         selected_button(data)
// }
//
// function disable_check(data) {
//     try {
//         data.filter(x => x.checked == false)[0].disabled=true;
//     }
//     catch (e) {
//     }
// }
//
// function enable_check(data) {
//     try {
//         data.filter(x => x.disabled == true)[0].disabled = false;
//     }
//     catch (e) {
//     }
// }
//
// function selected_button(data) {
//     let x = data.filter(x => x.checked == true)
//     if(x.length == 1){
//         alert("Mast have one correct answer")
//         data.filter(x => x.checked == true)[0].disabled = true
//     }
// }


        function validateForm(form)
        {
            var is_checked = 0
            var elem = document.getElementsByClassName("answers")
            for (var i = 0; i<elem.length; i++){
                if (elem[i].checked){
                    is_checked += 1;
                }
            }
            if(is_checked >= 1 && is_checked < elem.length)
            {
                document.getElementById('agree_chk_error').style.visibility='hidden';
                return true;
            }
            else if(is_checked == 0)
            {
                document.getElementById('agree_chk_error').style.visibility='visible';
                return false;
            }
            else if(is_checked == elem.length)
            {
                document.getElementById('agree_chk_error2').style.visibility='visible';
                return false;
            }

        }

        function validateFormResult(form)
        {
            var is_checked = 0
            var elem = document.getElementsByClassName("selected_values")
            for (var i = 0; i<elem.length; i++){
                if (elem[i].checked){
                    is_checked += 1;
                }
            }
            if(is_checked >= 1 && is_checked < elem.length)
            {
                document.getElementById('agree_chk_error').style.visibility='hidden';
                return true;
            }
            else if(is_checked == 0)
            {
                document.getElementById('agree_chk_error').style.visibility='visible';
                return false;
            }
            else if(is_checked == elem.length)
            {
                document.getElementById('agree_chk_error2').style.visibility='visible';
                return false;
            }

        }