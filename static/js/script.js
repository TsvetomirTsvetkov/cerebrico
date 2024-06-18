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

function sendForm(){    
    document.getElementById('formName').submit()
}

document.addEventListener("DOMContentLoaded", function() {
    // Get all checkboxes
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');

    // Add the event listener for each checkbox
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            // Access the hidden field with the same name
            var hiddenField = document.querySelector('input[type="hidden"][name="' + checkbox.name + '"]');


            if (hiddenField){
                // Modify the hidden field value based on the checkbox state
                if (checkbox.checked) {
                    hiddenField.value = '[CHCK]';
                } else {
                    hiddenField.value = '[UNCH]';
                }
                // Send form when checkbox selected
                sendForm();
            }
            

        });
    });
});



