const commentaryForm = document.getElementById('commentary-form')
const title = document.getElementById('title')
const commentary = document.getElementById('commentary')
const alertBox = document.getElementById('alert-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log('csrf: ', csrf[0].value)


commentaryForm.addEventListener('submit', e=>{
    console.log('Submit clicked')
    e.preventDefault()

    $.ajax({
        type: "POST",
        url: '/accounts/post_commentary/',
        data:{
            'csrfmiddlewaretoken':csrf[0].value,
            'title': title.value,
            'commentary':commentary.value
        },
        success: function(response){
            console.log(response)
            $("#modalCenter").modal('hide')
            handleAlerts('success', 'Blog Commentary added')
        },
        error: function(error){
            console.log(error)
            handleAlerts('danger', 'Oops... something went wrong')
        }
    })
})