$('#searchTour').click(function (){
    $.ajax('/', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'text': $('#searchText').val()
        },
        'success': function (response){
            let search = document.getElementById('search')
            search.innerHTML += `<p>${$('#searchText').val()}</p>` + search.innerHTML;
        }
    });
});

