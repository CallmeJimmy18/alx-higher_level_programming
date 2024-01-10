$('#add_item').on('click', function () {
  const item = $('<li>').text('Item');
  $('ul.my_list').append(item);
});
