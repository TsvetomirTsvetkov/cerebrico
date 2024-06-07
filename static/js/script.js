function deleteProfile() {
    var lang = document.documentElement.getAttribute('lang');

    if (lang == 'en'){
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