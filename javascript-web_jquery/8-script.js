const doc = window.$;
doc.get('https://swapi.co/api/films/?format=json', function (data) {
  for (const peli of data.results) {
    $('#list_movies').append(`<li>${peli.title}</li>`);
  }
});
