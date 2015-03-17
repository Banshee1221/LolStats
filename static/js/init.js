$(document).ready(function () {
    $('#butChange').click(function () {
        if ($('#nameIn').val() != '') {
            $('#butChange').html("<span class='glyphicon glyphicon-refresh glyphicon-refresh-animate'></span> Loading...")
        }
    });
    $('input[type=checkbox]').change(
    function(){
        if (this.checked) {
            alert('checked');
        }
        else {
            alert('unchecked');
        }
    });
});