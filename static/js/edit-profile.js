$('#editSave').click(function (){
    let data = new FormData();
    data.append('username', $('#editName').val());
    data.append('email', $('#editEmail').val());
    data.append('avatar', document.getElementById('avatar').files[0]);
    $.ajax('/profile/edit-profile', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': data,
        'processData': false,
        'contentType': false,
        'success': function (response){
            $('#user-username').html($('#editName').val());
            $('#user-email').html($('#editEmail').val());
            document.getElementById('user-avatar').src='avatar'
        },
        'error': function (a, b, errorType){
            if (errorType === 'Conflict'){
                $('#is_invalid_data').html('User or email already exists');
            }
        }
    });
});
