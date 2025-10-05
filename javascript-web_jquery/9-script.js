// Ensure the DOM is fully loaded
$(document).ready(function() {
  // API URL for hello translation
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

  // Fetch JSON data from the API
  $.getJSON(url, function(data) {
    // Display the value of 'hello' in DIV#hello
    $('#hello').text(data.hello);
  });
});
