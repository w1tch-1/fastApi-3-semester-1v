$('#sendComment').click(function (){
    let btn = $(this);
    $.ajax(btn.data('url'), {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'text': $('#postComment').val()
        },
        'success': function (response){
            let comments = document.getElementById('comment')
            comments.innerHTML += `<p>${$('#postComment').val()}</p>` + comments.innerHTML;
        }
    });
});
