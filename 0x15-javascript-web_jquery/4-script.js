#!/usr/bin/node
const $ = window.$;
$('DIV#toggle_header').click(function () {
  $('HEADER').toggleClass('green red');
});
