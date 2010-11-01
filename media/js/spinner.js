var newRequest = function(xhr_duration, spinner_delay, result, callback) {
    // because of eventual spinner delay useSpinner might not be used
    var spinner_timeout = false,
        spinner = new Spinner(result);
    new Request.HTML({
        url: '/echo/html/',
        data: {
            delay: xhr_duration,
            html: '<p>Data Loaded.</p>'
        },
        update: result,
        onSuccess: function() {
            clearTimeout(spinner_timeout);
            spinner.hide();
            result.highlight();
            if (callback) callback.call();
        }
    }).send();
    spinner_timeout = spinner.show.delay(spinner_delay*1000, spinner);
};
