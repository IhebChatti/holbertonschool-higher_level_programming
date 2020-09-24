const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=';
    const code = $('INPUT#language_code').val();
    $.get(url + code, (data) => {
      $('DIV#hello').html(data.hello);
    });
  });

  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
