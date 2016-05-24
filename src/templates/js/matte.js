(function worker() {
    $.ajax({
        url: 'matte-status',
        success: function(data) {
            console.log(data);
            if(data == 0) {
                window.location.reload();

            }
        },
        complete: function() {

            // Schedule the next request when the current one's complete
            setTimeout(worker, 1000);
        }
    });
})();

