$('#postSave').click(function (){
    let formData = new FormData();
    formData.append('text', $('#postText').val());
    formData.append('image', document.getElementById('postImage').files[0]);
    $.ajax('/post-create', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': formData,
        'processData': false,
        'contentType': false,
        'success': function (response){
               let posts = document.getElementById('posts')
            posts.innerHTML += `<h3>${$('#postText').val()}</h3>` + posts.innerHTML;
            posts.innerHTML += `<img src=${$('#postImage').val()}>` + posts.innerHTML;
            $('#postText').val('');
            // const postModal = new bootstrap.Modal('#postModal')
            // postModal.hide();
        }
    });
});
