$('.formset_row').formset({
    addText: '<i class="fa fa-plus" aria-hidden="true"></i>',
    deleteText: '<i style="color:red;" class="fa fa-trash-o" aria-hidden="true"></i>',
    prefix: 'movestocks_set'
});


// function CheckDuplicate(lid) {
//     var loacation_id;
//     $(".from_location").not(':last').each(function () {
//         loacation_id = $(this).val();
//         if (parseInt(loacation_id) == parseInt(lid)) {
//             sweetAlert({
//                 title: "Oops!",
//                 text: "Duplicate row not allowed!",
//                 type: "error"
//             });
//             $("tr:last").prev().remove();
//         }
//     });
// }
//
//
function InputBg() {
    $(function () {
        $(document).on('focus', '.product', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.product', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '.discount', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.discount', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '.from_location', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.from_location', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '.to_location', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.to_location', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '.qtymoved', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.qtymoved', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '.note', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.note', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });
}

$(document).ready(function () {
    $(".product").chosen({search_contains: true, no_results_text: "Oops, nothing found!", width: "100%"});
    InputBg();
     //hide last tr
    $(".dynamic-form-add").hide();

    //select value on click
    $(function () {
        $(document).on('click', 'input[type=text], input[type=number]', function () {
            this.select();
        });
    });
//
//     var trid;
//     var prePopulate;
//     var location_id_from;
//     var location_id_to;
//     var qtypresent;
//     var qtymoved;
//
//     $(document).on("change", ".from_location", function () {
//
//         trid = $(this).parents("tr").index();
//
//         location_id_from = $(this).val();
//
//         $.ajax({
//             url: '/get_stock?id=' + location_id_from,
//             type: 'GET',
//             success: function (data) {
//
//                 prePopulate = $.parseJSON(data);
//                 $(".qtypresent").eq(trid).val(prePopulate[0].qty.tot_qty);
//                 CheckDuplicate(location_id_from);
//
//                 $(".dynamic-form-add .add-row").click();
//             },
//             error: function (data) {
//                 sweetAlert({
//                     title: "Oops!",
//                     text: "No any product in stock!",
//                     type: "error"
//                 });
//             }
//         });
//
//         // location_id_to = $(".to_location").eq(trid).val();
//         //
//         // if (location_id_from == location_id_to) {
//         //     sweetAlert({
//         //         title: "Oops!",
//         //         text: "Same location not allowed",
//         //         type: "error"
//         //     });
//         //     $(this).find('option:first').prop('selected', 'selected');
//         // }
//
//
//     });
//
    $(document).on("change", ".to_location", function () {

        trid = $(this).parents("tr").index();
        location_id_from = $(".from_location").eq(trid).val();
        location_id_to = $(this).val();
        if (location_id_from == location_id_to) {
            sweetAlert({
                title: "Oops!",
                text: "Same location not allowed",
                type: "error"
            });
            $(this).find('option:first').prop('selected', 'selected');
        }

    });


// }));
//
//
    $(document).on("keyup", ".qtymoved", function () {
        trid = $(this).parents("tr").index();
        qtypresent = $(".qtypresent").eq(trid).val();
        qtymoved = $(this).val();
        if (parseInt(qtymoved) > parseInt(qtypresent)) {
            sweetAlert({
                title: "Oops!",
                text: "Qty moved can't be greater than Qty present!",
                type: "error"
            });
            $(this).val(qtypresent);
        }

    });

    $(".from_location").empty();

    $(document).on("change", ".product", function () {
        var prePopulate;
        var request_url;
        var id = $(this).val();
        var trid = $(this).parents("tr").index();

        request_url = '/stocktransfers/get_sum_product?id=' + id;
        $.ajax({
            type: 'GET',
            url: request_url,
            success: function (data) {
                prePopulate = $.parseJSON(data);
                $('#id_movestocks_set-0-qty_total').val(prePopulate[0].tot_p.tot_p);
            }
        });


        $(".from_location").eq(trid).empty();
        request_url = '/stocktransfers/get_location?id=' + id;
        $.ajax({
            type: 'GET',
            url: request_url,
            success: function (data) {
                var vals = '<option selected="selected" value="" disabled="disabled">Please select a location</option>';
                prePopulate = $.parseJSON(data);
                $.each(prePopulate, function (key, value) {
                    vals += '<option value="' + value.location_id + '">' + value.location_name + '</option>';
                });
                $(".from_location").eq(trid).html(vals);

            }
        });
        $('#id_movestocks_set-0-from_location').focus();
        $('#id_movestocks_set-0-qtypresent').val(0);

    });


    $(document).on("change", ".from_location", function () {
        var trid = $(this).parents("tr").index();

        location_id_to = $(".to_location").eq(trid).val();
        location_id_from = $(this).val();
        if (location_id_from == location_id_to) {
            sweetAlert({
                title: "Oops!",
                text: "Same location not allowed",
                type: "error"
            });
            $(".to_location").eq(trid).find('option:first').prop('selected', 'selected');
        }


        var lid = $(this).val();
        var id = $(".product").eq(trid).val();
        var request_url = '/stocktransfers/get_tot_product?lid=' + lid + '&id=' + id;
        $.ajax({
            type: 'GET',
            url: request_url,
            success: function (data) {

                prePopulate = $.parseJSON(data);
                $(".qtypresent").eq(trid).val(prePopulate[0].tot_product.tot_product);
            }
        });
        $('#id_movestocks_set-0-to_location').focus();
    });


    $(document).on("change", ".to_location", function () {

        $('#id_movestocks_set-0-qtymoved').focus();
        $('#id_movestocks_set-0-qtymoved').select();
    });
});


