$(document).ready(function(){
    $('.scrollspy').scrollSpy();

    $(window).on('scroll', function() {
        scrollPosition = $(this).scrollTop();
        if (scrollPosition >= 100) {
            // If the function is only supposed to fire once
            $("#toc").css("position", "fixed").css("top", "20px");
        }
        else {
            $("#toc").css("position", "absolute").css("top", "70px");
        }
    });
    document.getElementById('vid1').addEventListener('loadedmetadata', function() {
        this.currentTime = 0.01;
    }, false);

});