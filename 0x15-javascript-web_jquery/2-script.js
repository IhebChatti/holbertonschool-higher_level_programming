#!/usr/bin/node
const $ = window.$;
$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});