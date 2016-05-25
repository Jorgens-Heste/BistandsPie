(function worker() {
    $.ajax({
        url: 'matte-status',
        success: function(data) {
            console.log(data);
            if(data == 0) {
                body = $('body,html') // get body
                body.css('background-color', 'black');
                body.empty(); // Empty all text

                window.location.reload();

            }
        },
        complete: function() {

            // Schedule the next request when the current one's complete
            setTimeout(worker, 500);
        }
    });
})();

