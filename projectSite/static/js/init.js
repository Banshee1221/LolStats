$(document).ready(function(){
    $('.scrollspy').scrollSpy();

    $(window).on('scroll', function() {
        scrollPosition = $(this).scrollTop();
        if (scrollPosition >= 125) {
            // If the function is only supposed to fire once
            $("#toc").css("position", "fixed").css("top", "0px");

            // Other function stuff here...
        }
        else {
            $("#toc").css("position", "absolute").css("top", "85px");
        }
    });
});