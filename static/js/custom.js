$(document).ready(function () {
    $('.user-menu').mouseenter(function () {
        $('.dropdown-menu-right').show();
        $('.dropdown-menu-right').mouseleave(function () {
            $(this).hide();
        });

    });
// on all invoice forms
    $("#id_discount_total").prop('readonly', true);
    $("#id_amount").prop('readonly', true);
    $("#id_previous_balance").prop('readonly', true);
    $("#id_net_amount").prop('readonly', true);
    $("#id_balance").prop('readonly', true);

    // stock transfer
    $("#id_movestocks_set-0-qtypresent").prop('readonly', true);
    $("#id_movestocks_set-0-qty_total").prop('readonly', true);

    // width
    $(".location").css({'width': 100});
    $(".status").css({'width': 100});
});
