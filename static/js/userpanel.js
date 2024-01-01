function Send_ticket() {

    if (document.getElementById("tickettxt").value != "" &&  document.getElementById("ticketreson").value != "" ) {

        $.ajax({
            type: 'POST',
            url: 'connect',
            data: {
                ticet_text: $('#tickettxt').val(),
                ticetreson: $('#ticketreson').val(),
                sender: $('#username').val() ,
            },
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function () {
                console.log($('#ticketreson').val())
                window.location = "/accounts/profile/Dashbord"
            },


        });

    }

}




document.getElementById("ShowSideMenu").addEventListener("click", function () {
    document.getElementById("side-menu").classList.toggle("sidehide")
})


document.getElementById("HidMenu").addEventListener("click", function () {
    document.getElementById("side-menu").classList.toggle("sidehide")
})
