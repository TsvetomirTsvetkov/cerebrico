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
