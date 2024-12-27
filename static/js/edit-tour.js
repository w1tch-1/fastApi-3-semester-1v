$('#editSave').click(function (){
    let data = new FormData();
    let btn = $(this);
    data.append('title', $('#editTitle').val());
    data.append('text', $('#editText').val());
    data.append('price', $('#editPrice').val());
    $.ajax(btn.data('url'), {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': data,
        'processData': false,
        'contentType': false,
        'success': function (response){
            $('#tour-title').html($('#editTitle').val());
            $('#tour-text').html($('#editText').val());
            $('#tour-price').html($('#editPrice').val());
        }
    });
})