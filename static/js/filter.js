var filter = document.getElementById("NorNCS");
//
// filter.addEventListener("change",function() {
//
//     var x = filter.value;
//
//
//     if (filter.value == 1) {
//         document.getElementById("news").classList.remove("d-none")
//         document.getElementById("newch").classList.add("d-none")
//         document.getElementById("newch1").classList.remove("d-none")
//         document.getElementById("storylist").classList.add("d-none")
//         document.getElementById("chapterlist").classList.add("d-none")
//         document.getElementById("summary").classList.remove("d-none")
//         document.getElementById("ganer").classList.remove("d-none")
//
//
//     }
//     if (filter.value == 2) {
//         document.getElementById("news").classList.add("d-none")
//         document.getElementById("newch").classList.remove("d-none")
//         document.getElementById("storylist").classList.remove("d-none")
//         document.getElementById("newch1").classList.add("d-none")
//         document.getElementById("chapterlist").classList.add("d-none")
//         document.getElementById("summary").classList.add("d-none")
//         document.getElementById("ganer").classList.add("d-none")
//         document.getElementById("ganer").classList.add("d-none")
//
//
//     }
//     if (filter.value == 3) {
//         document.getElementById("news").classList.add("d-none")
//         document.getElementById("newch").classList.add("d-none")
//         document.getElementById("storylist").classList.remove("d-none")
//         document.getElementById("newch1").classList.add("d-none")
//         document.getElementById("chapterlist").classList.remove("d-none")
//         document.getElementById("summary").classList.add("d-none")
//         document.getElementById("ganer").classList.add("d-none")
//
//
//
//     }
//
//
// })

function Create_Story() {

    if (document.getElementById("news").value != "" && document.getElementById("ganer").value != "ganer" && document.getElementById("summary").value != "" ) {

        $.ajax({
            type: 'POST',
            url: 'newstory',
            data: {
                username: $('#writer_name').val(),
                StoryTitel: $('#news').val(),
                ganer: $('#ganer').val(),
                summary: $('#summary').val(),
            },
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function () {
                window.location = "/WriteStory"
            },


        });

    }

}


function Create_Chapter() {


    $.ajax({
        type: 'POST',
        url: '/WriteStory/',
        data: {
            username: $('#writer_name').val(),
            ChapterTitel: $('#newch').val(),
            ForStory: $('#ForStory').val(),
            Section: $('#Section').val(),

        },
        headers: {
            'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function () {
            window.location = "/accounts/profile/Dashbord"
        },


    });

}
//
// console.log(document.getElementById('storylist').value)
