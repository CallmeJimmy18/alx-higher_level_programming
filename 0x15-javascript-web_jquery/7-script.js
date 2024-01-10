$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (element) {
    $('#character').text(element.name);
  }
});
