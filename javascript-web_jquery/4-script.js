const doc = window.$;
doc('#toggle_header').click(function () {
  doc('header').toggleClass('red');
  doc('header').toggleClass('green');
});
