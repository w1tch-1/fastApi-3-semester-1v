$('#searchTour').click(function (){
    $.ajax('/', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'text': $('#searchText').val()
        },
        'success': function (response){
            let comments = document.getElementById('comment')
            comments.innerHTML += `<p>${$('#postComment').val()}</p>` + comments.innerHTML;
        }
    });
});

