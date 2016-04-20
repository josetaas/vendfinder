$(document).ready(function () {
    var user = $('#user').data().name;
    var ajax_script = $SCRIPT_ROOT + '/' + user + '/get_config';
    $(function get_config() {
        $.getJSON(ajax_script, function(data) {
            $('textarea#config').val(data);
        });
    });
});
