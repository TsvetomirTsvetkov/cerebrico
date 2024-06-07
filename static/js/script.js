function deleteProfile() {
    // var language = JSON.parse("{{ LANGUAGE_CODE|escapejs }}");
    //console.log({{LANGUAGE_CODE}});
    // var language = document.getElementById('lang').getAttribute('data-variable');
    var language = document.getElementsByTagName('html')[0].getAttribute('lang');
    console.log(language)
    if (language == 'gb'){
        if (confirm("Do you really want to delete your profile?")) {
            location.href = '/profile/delete';
        }
    }
    else {
        if (confirm("Наистина ли искате да изтриете профила си?")) {
            location.href = '/profile/delete';
        }
    }
    
}



function completeTask(str){
    // var variable = document.getElementById("tasks");

    var inputs = document.querySelectorAll("input[type='checkbox']");
    for(var i = 0; i < inputs.length; i++) {
        if (inputs[i].checked){
            console.log(inputs[i].id)
            console.log(inputs[i].value)
        }
    }
}