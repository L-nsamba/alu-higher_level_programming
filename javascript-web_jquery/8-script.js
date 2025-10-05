// Wait until the DOM is fully loaded
$(document).ready(function() {
  // URL of the Star Wars films API
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Fetch JSON data from the API
  $.getJSON(url, function(data) {
    // Loop through each movie in the results
    data.results.forEach(function(movie) {
      // Append each movie title as a list item in UL#list_movies
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
