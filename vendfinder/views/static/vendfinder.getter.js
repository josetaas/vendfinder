$( document ).ready(function() {
    var user = $('#user').data().name;
    var ajax_script = $SCRIPT_ROOT + '/' + user + '/get_vendors';
    $(function get_vendors() {
        $.getJSON(ajax_script, function(data) {
            if (ischanged(data)) {
                var audio = new Audio($SCRIPT_ROOT + '/static/' + 'pling.mp3');
                audio.play();
            }

            lastData = data;
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
        setTimeout(get_vendors, 2000);
    });
});

function ischanged(data) {
    if (data.length > 0 && (typeof lastData === 'undefined' ||
        lastData.length == 0)) {
        return true;
    }

    for (i = 0; i < data.length; i++) {
        for (j = 0; j < lastData.length; j++) {
            if (data[i]['item'] == lastData[j]['item'] &&
                    data[i]['shop'] == lastData[j]['shop']) {
                break;
            }

            if (j == lastData.length - 1) {
                return true;
            }
        }
    }

    return false;
}
