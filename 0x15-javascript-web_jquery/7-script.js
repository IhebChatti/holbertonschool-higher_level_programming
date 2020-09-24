const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  $('DIV#update_header').text(data.name);
});
