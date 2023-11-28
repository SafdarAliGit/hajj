$(document).on("click", "#menubutton-plus", function () {
    $('#ddmenu .dropdown').toggle();
    $('#quickmenubutton-plus').toggleClass('quickmenubutton');

});

$(document.body).click(function () {
    $('#ddmenu .dropdown').hide();
    $('#quickmenubutton-plus').removeClass('quickmenubutton');
});


$('#menubutton-home').click(function () {
    $('#quickmenubutton-home').toggleClass('quickmenubutton');
});

$('#menubutton-gear').click(function () {
    $('#quickmenubutton-gear').toggleClass('quickmenubutton');
});

$('.dismissit').click(function () {
    $('#ddmenu .dropdown').hide();
});

