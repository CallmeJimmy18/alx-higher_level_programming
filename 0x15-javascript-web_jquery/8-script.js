$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (response) {
    $.each(response.results, function (index, movie) {
      const movietitle = $('<li>').text(movie.title);
      $('#list_movies').append(movietitle);
    });
  }
});
