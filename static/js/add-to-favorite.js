document.addEventListener("DOMContentLoaded", function() {
    const userId = {{ user.id }};
    const postId = {{ current_post.id }};
    document.getElementById("addFavoriteBtn").addEventListener("click", function() {
        $.ajax({
            url: '/add_to_favorites/',
            type: 'POST',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify({
                user_id: userId,
                post_id: postId
            }),
            success: function(response) {
                alert(response.message);
            },
            error: function(error) {
                alert(error.responseJSON.detail || 'An error occurred.');
            }
        });
    });
});
