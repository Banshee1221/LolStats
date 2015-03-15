$(document).ready(function () {
    $('#butChange').click(function () {
        if ($('#nameIn').val() != '') {
            $('#butChange').html("<span class='glyphicon glyphicon-refresh glyphicon-refresh-animate'></span> Loading...")
        }
    });
    $('#rightDiv').click(function(e) {
        if ($(e.target).hasClass('padder'))
            alert("test!");
    });
});