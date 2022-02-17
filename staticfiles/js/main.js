$(document).ready(function () {
  var showform = $("#show_form");
  var hideform = $("#hide_form");
  var commentform = $("#comment_form");

  commentform.hide();

  showform.click(function () {
    commentform.slideToggle();
  });

  hideform.click(function () {
    commentform.slideUp();
  });
});
