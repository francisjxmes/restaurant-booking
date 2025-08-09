$(document).ready(function () {
  $('.tab-link').click(function (e) {
    e.preventDefault();

    const target = $(this).data('tab');

    // Hide all sections
    $('.menu-section').hide();

    // Remove active class from all tabs
    $('.tab-link').removeClass('active');

    // Show the selected tab and mark it active
    $('#' + target).fadeIn(200);
    $(this).addClass('active');
  });
});