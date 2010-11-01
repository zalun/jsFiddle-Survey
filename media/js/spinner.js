var clearRequest = function(result, response, spinner_timeout, spinner, callback) {
  result.set('html', response);
  clearTimeout(spinner_timeout);
  spinner.hide();
  result.highlight();
  if (callback) callback.call();
}
var newRequest = function(xhr_duration, spinner_delay, result, callback) {
    // because of eventual spinner delay useSpinner might not be used
    var spinner = new Spinner(result);
    callback = callback || false;

    clearRequest.delay(xhr_duration*1000, this, [
        result, 
        '<p>Data loaded</p>', 
        spinner.show.delay(spinner_delay*1000, spinner),
        spinner,
        callback
        ]);
};
