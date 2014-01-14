$(function() {
    $('.token_field').selectize({
        plugins: ['remove_button'],
        delimiter: ',',
        persist: false,
        preload: true,
        create: function(input) {
            return {
                value: input,
                text: input
            }
        },
        load: function(query, callback) {
            $.getJSON('/languages').then(function(data) {
                callback(data);
            });
        },
        onChange: function(value) {
            debugger
        }
    });
});
