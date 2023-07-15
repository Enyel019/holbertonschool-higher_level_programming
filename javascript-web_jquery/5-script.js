const doc = window.$;
doc('#add_item').click(function () {
  doc('UL.my_list').append('<li>Item</li>');
});
