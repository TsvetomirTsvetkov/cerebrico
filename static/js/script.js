function deleteProfile() {
    if (confirm("Do you really want to delete your profile?")) {
        location.href = '/profile/delete';
    }
}

function findId(){
    let array = [
        { id: 1, name: 'John' },
        { id: 2, name: 'Jane' },
        { id: 3, name: 'Joe' }
    ];
    
    let result = array.find(obj => obj.id === 2);
    
    console.log(result);
}