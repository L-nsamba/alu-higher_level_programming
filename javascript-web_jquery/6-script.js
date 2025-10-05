// Wait until the DOM is fully loaded
$(document).ready(function() {
  // Attach a click event handler to the DIV with id "update_header"
  $('#update_header').click(function() {
    // Update the text of the <header> element
    $('header').text('New Header!!!');
  });
});
