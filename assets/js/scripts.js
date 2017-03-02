$(document).ready(function() {
    $(window).endlessScroll({
        inflowPixels: 200,
        callback: function() {
            var $img = $('#img-container').clone();
            $('#image-scroll').append($img);
        }
    });
});

