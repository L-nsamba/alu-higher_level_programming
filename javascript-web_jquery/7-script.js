// Wait until the DOM is fully loaded
$(document).ready(function() {
  // URL of the Star Wars API
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Fetch data from the API using jQuery's getJSON method
  $.getJSON(url, function(data) {
    // Update the DIV#character with the character name
    $('#character').text(data.name);
  });
});
