$('#deleteTour').click(function () {
    let btn = $(this);
    $.ajax({
        url: btn.data('url'),
        type: 'POST',
        dataType: 'json',
        success: function (response) {
            alert('Tour deleted successfully');
            location.reload();
        },
        error: function (xhr, status, error) {
            alert('Failed to delete the tour: ' + error);
        }
    });
});