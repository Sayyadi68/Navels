// send phone number to jango 09333333333 

function send_ponenumber() {
    $.ajax({
        type: 'POST',
        url: '/login/',
        data: {
            phone_number: $('#validation-phonenumber').val(),
        },
        headers: {
            'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function () {
            document.getElementById("btn-hide").click();
        },

    });
    document.getElementById("btn-hide").click();

    // add phone_number to next modal to title phone number
    document.getElementById("form-code-titel-phone_number").innerText = $('#validation-phonenumber').val();

}


// function countdown timer;

// if you click to ارسال مجدد کد
function sned_retern_sms() {
    send_ponenumber();
    document.getElementById("btn-hide").click();
    document.getElementById("p_sned_retern").classList.remove("d-inline");
    document.getElementById("p_sned_retern").classList.add("d-none");
    document.getElementById("wait_countdown_timer").classList.remove("d-none");
}

// if click to button ورود i go you to without page
function send_code() {
    $.ajax({
        type: 'POST',
        url: '/verify_login/',
        data: {
            otp: $('#import_code').val(),
        },
        headers: {
            'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function (data) {
            window.location = ''
        },
        error: function (data) {
            alert(data.responseJSON.error);
        }


    });
}

// it is for check input phone number to we import corrent kind number

function check_input_send_phonenumber() {
    let input_phonenumber = $('#validation-phonenumber').val();

    if (input_phonenumber.length == 11 && input_phonenumber.charAt(0) == 0 && input_phonenumber.charAt(1) == 9) {
        document.getElementById("btnSend").classList.remove("btn-secondary");
        document.getElementById("btnSend").classList.add("btn-success");
        document.getElementById("btnSend").removeAttribute("disabled");
    } else if (input_phonenumber.length == 10 && input_phonenumber.charAt(0) == 9) {
        document.getElementById("btnSend").classList.remove("btn-secondary");
        document.getElementById("btnSend").classList.add("btn-success");
        document.getElementById("btnSend").removeAttribute("disabled");
    } else if (input_phonenumber.length == 12 && input_phonenumber.charAt(0) == 9 && input_phonenumber.charAt(1) == 8) {
        document.getElementById("btnSend").classList.remove("btn-secondary");
        document.getElementById("btnSend").classList.add("btn-success");
        document.getElementById("btnSend").removeAttribute("disabled");
    } else if (input_phonenumber.length == 0) {
        document.getElementById("btnSend").setAttribute("disabled", "0");
        document.getElementById("btnSend").classList.remove("btn-success");
        document.getElementById("btnSend").classList.add("btn-secondary");
    } else {
        document.getElementById("btnSend").setAttribute("disabled", "0");
        document.getElementById("btnSend").classList.remove("btn-success");
        document.getElementById("btnSend").classList.add("btn-secondary");

    }
}


function check_input_send_code() {
    let input_code = $('#import_code').val();
    if (input_code.length == 5) {
        document.getElementById("btn_send_code").classList.remove("btn-secondary");
        document.getElementById("btn_send_code").classList.add("btn-success");
        document.getElementById("btn_send_code").removeAttribute("disabled");
    } else {
        document.getElementById("btn_send_code").setAttribute("disabled", "0");
        document.getElementById("btn_send_code").classList.remove("btn-success");
        document.getElementById("btn_send_code").classList.add("btn-secondary");
    }

}

//btn send
document.getElementById("btnSend").setAttribute("disabled", "0");
document.getElementById("btnSend").classList.remove("btn-success");
document.getElementById("btnSend").classList.add("btn-secondary");
// btn import code
document.getElementById("btn_send_code").setAttribute("disabled", "0");
document.getElementById("btn_send_code").classList.remove("btn-success");
document.getElementById("btn_send_code").classList.add("btn-secondary");


//
// document.addEventListener("contextmenu", (e) =>{
//   e.preventDefault()
// }
// )
//
// $(document).bind('keydown', function(e) {
//   if(e.ctrlKey && (e.which == 83)) {
//     e.preventDefault();
//     return false;
//   }
// });


window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove();
    });
}, 4000);