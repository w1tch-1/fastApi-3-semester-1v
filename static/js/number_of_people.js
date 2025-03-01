$('#NumberOfPeople').click(function () {
    let btn = $(this);
    let peopleValue = $('#people').val();
    let url = `${btn.data('url')}?people=${peopleValue}`;

    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        success: function (response) {
            if (response.error) {
                alert(response.error);
            } else {
                $('#total').html(response.result + '€');
            }
        },
        error: function () {
            alert('An error occurred. Please try again.');
        }
    });
});
