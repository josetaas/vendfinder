$( document ).ready(function() {
    var user = $('#user').data().name;
    var ajax_script = $SCRIPT_ROOT + '/' + user + '/get_vendors';
    $(function get_vendors() {
        $.getJSON(ajax_script, function(data) {
            $('#vendors tbody tr').remove();
            for (shop in data) {
                var row = ''
                row += '<tr><td>' + data[shop]['item'] + '</td>';
                row += '<td>' + data[shop]['amount'] + '</td>';
                row += '<td>' + data[shop]['price'] + 'z</td>';
                row += '<td>' + data[shop]['shop'] + '</td>';
                row += '<td>' + data[shop]['map'] + '</td></tr>';
                $('#vendors tbody').append(row);
            }
        });
        setTimeout(get_vendors, 5000);
    });
});
