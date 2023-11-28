$('.formset_row').formset({
    addText: '<i class="fa fa-plus" aria-hidden="true"></i>',
    deleteText: '<i style="color:red;" class="fa fa-trash-o" aria-hidden="true"></i>',
    prefix: 'salesr_set'
});


// current element bg color
function InputBg() {

    $(function () {
        $(document).on('focus', '.status', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.status', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });
    $(function () {
        $(document).on('focus', '.location', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.location', function () {
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
        $(document).on('focus', '.barcode', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.barcode', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '.qtyreturned', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.qtyreturned', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '.price', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.price', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '.discount_cur', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '.discount_cur', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });


    $(function () {
        $(document).on('focus', '#id_paid', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '#id_paid', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });


    $(function () {
        $(document).on('focus', '#id_cdate', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '#id_cdate', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '#id_duedate', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '#id_duedate', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

    $(function () {
        $(document).on('focus', '#id_sale_type', function () {
            $(this).css({'background-color': 'rgb(200,250,200)'});
        });
    });
    $(function () {
        $(document).on('blur', '#id_sale_type', function () {
            $(this).css({'background-color': 'rgb(255,255,255)'});
        });
    });

}

//calculations function declaratioon
function Calculations(rowID) {
    //row calculations
    var discount_percent = 0;
    var price = 0;
    var qty_returned;
    var discount_value_sum = 0;
    var sum = 0;
    var discount = 0;
    var net = 0;
    var discount_value;
    var net_after_discount;
    var leg_balance;
    var amount;
    var paid;
    var balance;

    qty_returned = $("#" + rowID + " .qtyreturned").val();
    discount_percent = $("#" + rowID + " .discount").val();
    price = $("#" + rowID + " .price").val();
    net = parseInt(qty_returned) * parseFloat(price).toFixed(3);
    discount_value = net * (discount_percent / 100);

    $(".discount_cur").each(function () {
        discount_value_sum += parseFloat($(this).val()) || 0;
    });

    net_after_discount = net - discount_value || 0.000;
    $("#" + rowID + " .net").val(parseFloat(net_after_discount).toFixed(3));
    $(".net").each(function () {
        sum += parseFloat($(this).val()) || 0;
    });

    //sum of net amount on detail form end
    $('#id_amount').val(parseFloat(sum).toFixed(3));
    $('#id_total').val(parseFloat(sum).toFixed(3));
    $('#id_balance').val(parseFloat(sum).toFixed(3));
    $('#id_net_amount').val(parseFloat(sum).toFixed(3));
    $('#id_discount_total').val(parseFloat(discount_value_sum).toFixed(3));

    leg_balance = $('#id_previous_balance').val();
    amount = $('#id_amount').val();
    paid = $('#id_paid').val();
    net = parseFloat(amount) + parseFloat(leg_balance);
    $('#id_net_amount').val(net);
    balance = net - parseFloat(paid);
    $('#id_balance').val(balance);
}

// on keypup calculations
function SubCalculations(rowID) {
    var qtyreturned;
    var price;
    var d_p;
    var d;
    var net;
    d_p = $("#" + rowID + " .discount").val();
    qtyreturned = $("#" + rowID + " .qtyreturned").val();
    price = $("#" + rowID + " .price").val();
    net = parseInt(qtyreturned) * parseFloat(price).toFixed(3);
    d = net * (d_p / 100) || 0.000;
    $("#" + rowID + " .discount_cur").val(parseFloat(d).toFixed(3));

}

// object definition
var Obj = {
    arr: [],
    subObj: {},
    add: function (r, p, b) {
        this.subObj = {};
        this.subObj.row = r;
        this.subObj.product = p;
        this.subObj.barcode = b;
        this.arr.push(this.subObj);
    },
    find_id: function (id) {
        for (var i = 0, l = this.arr.length; i < l; i++) {
            if (this.arr[i].product == id) {
                return this.arr[i];
            }
        }
        return undefined;
    },
    find_barcode: function (b) {
        for (var i = 0, l = this.arr.length; i < l; i++) {
            if (this.arr[i].barcode == b) {
                return this.arr[i];
            }
        }
        return undefined;
    },
    remove: function (id) {
        for (var i = 0, l = this.arr.length; i < l; i++) {
            if (this.arr[i].product == id) {
                this.arr.splice(i, 1);
                break;
            }
        }


    }
};

$(document).ready((function () {
    // delete object of row from Obj
    $('.delete-me').click(function () {
        // variable delarations
        var discount_value_sum = 0;
        var sum = 0;
        var leg_balance = 0;
        var amount = 0;
        var received = 0;
        var balance = 0;
        var net_value = 0;

        var trid = $(this).parents("tr").attr("id");
        var p_id = $("#" + trid + " .product").val();

        $(".discount_cur").each(function () {
            discount_value_sum += parseFloat($(this).val()) || 0;
        });

        $("#" + trid + " .net").removeClass('net');
        $(".net").each(function () {
            sum += parseFloat($(this).val()) || 0;
        });

        //sum of net amount on detail form end
        $('#id_amount').val(parseFloat(sum).toFixed(3));
        $('#id_total').val(parseFloat(sum).toFixed(3));
        $('#id_balance').val(parseFloat(sum).toFixed(3));
        $('#id_net_amount').val(parseFloat(sum).toFixed(3));
        $('#id_discount_total').val(parseFloat(discount_value_sum).toFixed(3));

        leg_balance = $('#id_previous_balance').val();
        amount = $('#id_amount').val();
        received = $('#id_received').val();
        net_value = parseFloat(amount) + parseFloat(leg_balance);
        $('#id_net_amount').val(net_value);
        balance = net_value - parseFloat(received);
        $('#id_balance').val(balance);

        Obj.remove(p_id);
    });

    // disable scroll on date
    $('#id_cdate, #id_duedate').bind("mousewheel", function () {
        return false;
    });
    // make product list enable
    $(document).on("click", "#salereturn_button", function () {
        $(".product").not(':last').prop("disabled", false).trigger("chosen:updated");
        $('#salereturn_form').submit();
    });
    // move amount value to right
    $('#id_amount').addClass('text-right');
    //hide last tr
    $(".dynamic-form-add").hide();

    //current item background color
    InputBg();
    //select value on click
    $(function () {
        $(document).on('click', 'input[type=text], input[type=number]', function () {
            this.select();
        });
    });
    //to stop scrol on date inputs

    $("#id_customer").chosen({search_contains: true, no_results_text: "Oops, nothing found!", width: "100%"});

    // choosen
    $(".product").chosen({search_contains: true, no_results_text: "Oops, nothing found!", width: "100%"});
    setTimeout(function () {
        $("input.barcode:first").focus();
    }, 1000);


    $('#id_cdate, #id_duedate').datetimepicker({
        format: "Y-m-d h:m:s",
        onShow: function (ct) {

        },
        timepicker: false
    });

    // balance calculation
    $(document).on("keyup", "#id_paid", function () {
        var net_amount;
        var paid;
        var balance;
        // check on received

        var a = $('#id_amount').val();
        var r = $("#id_paid").val();
        if (parseInt(r) > parseInt(a)) {
            sweetAlert({
                title: "Oops!",
                text: "Paid amount can't greater than invoice amount!",
                type: "error"
            });
            $("#id_paid").val(a);

            // balance calculations
            net_amount = $('#id_net_amount').val();
            paid = $('#id_paid').val();
            balance = parseFloat(net_amount) - parseFloat(paid);
            $('#id_balance').val(parseFloat(balance).toFixed(3));

        } else if ((parseInt(r) <= 0) || (r == '')) {
            sweetAlert({
                title: "Oops!",
                text: "Paid amount can't be 0 less than zero !",
                type: "error"
            });
            $("#id_paid").val(0);
        }

        net_amount = $('#id_net_amount').val();
        paid = $('#id_paid').val();
        balance = parseFloat(net_amount) - parseFloat(paid);
        $('#id_balance').val(parseFloat(balance).toFixed(3));

    });
    //price and quantity multiplication
    $(document).on("keyup", ".qtyreturned", function () {
        var trid = $(this).parents("tr").attr("id");

        SubCalculations(trid);
        Calculations(trid);

        var q = $(this).val();
        if ((parseInt(q) <= 0) || (q == '')) {
            sweetAlert({
                title: "Oops!",
                text: "Selling qty can't be 0 less than zero !",
                type: "error"
            });
            $(this).val(1).select();

            SubCalculations(trid);
            Calculations(trid);
        }

    });
    //price calculations
    $(document).on("keyup", ".price", function () {
        var trid = $(this).parent().parent("tr").attr("id");
        var qtysold;
        var price;
        var d_p;
        var d;
        var net;
        d_p = $("#" + trid + " .discount").val();
        qtysold = $("#" + trid + " .qtyreturned").val();
        price = $("#" + trid + " .price").val();
        net = parseInt(qtysold) * parseFloat(price).toFixed(3);
        d = net * (d_p / 100) || 0.000;
        $("#" + trid + " .discount_cur").val(parseFloat(d).toFixed(3));

        Calculations(trid);

        var p_id = $("#" + trid + " .product").val();

        $.ajax({
            url: '/salesreturn/sprice?id=' + p_id,
            type: 'GET',
            success: function (data) {

                var prePopulate = $.parseJSON(data);
                var pp = prePopulate[0].purchase_price;
                if (parseFloat(price) < parseFloat(pp)) {
                    sweetAlert({
                        title: "Oops!",
                        text: "Selling price can't be less than purchase price !",
                        type: "error"
                    });


                    d_p = $("#" + trid + " .discount").val();
                    qtysold = $("#" + trid + " .qtyreturned").val();
                    price = $("#" + trid + " .price").val();
                    net = parseInt(qtysold) * parseFloat(price).toFixed(3);
                    d = net * (d_p / 100) || 0.000;
                    $("#" + trid + " .discount_cur").val(parseFloat(d).toFixed(3));

                    Calculations(trid);
                }

            },
            error: function (data) {
                sweetAlert({
                    title: "Oops!",
                    text: "No any product in stock under this product ID!",
                    type: "error"
                });
            }
        });

    });
    //discounts in currency calculations
    $(document).on("keyup", ".discount", function () {
        var trid = $(this).parent().parent("tr").attr("id");

        SubCalculations(trid);
        Calculations(trid);

        // check on qtysold
        var discount_p = $(this).val();
        if ((parseInt(discount_p) < 0) || (discount_p == '') || (parseInt(discount_p) >= 100)) {
            sweetAlert({
                title: "Oops!",
                text: "Discount%  can't be less than zero or equal to or greater than 100 !",
                type: "error"
            });
            $(this).val(parseFloat(0).toFixed(3)).select();

            SubCalculations(trid);
            Calculations(trid);
        }


    });
    //discounts in percent calculations
    $(document).on("keyup", ".discount_cur", function () {
        var trid = $(this).parent().parent("tr").attr("id");
        var qtysold;
        var price;
        var net;
        var discount_percent;
        var d_amount;
        d_amount = $("#" + trid + " .discount_cur").val();
        qtysold = $("#" + trid + " .qtyreturned").val();
        price = $("#" + trid + " .price").val();
        net = parseInt(qtysold) * parseFloat(price).toFixed(3);
        discount_percent = parseFloat((d_amount * 100) / net).toFixed(3) || 0.000;
        $("#" + trid + " .discount").val(discount_percent);
        Calculations(trid);

        var discount_c = $(this).val();
        if ((parseInt(discount_c) < 0) || (discount_c == '') || (parseInt(discount_c) >= net)) {
            sweetAlert({
                title: "Oops!",
                text: "Discount%  can't be less than zero or equal to or greater than net value !",
                type: "error"
            });
            $(this).val(parseFloat(0).toFixed(3)).select();

            d_amount = $("#" + trid + " .discount_cur").val();
            qtysold = $("#" + trid + " .qtyreturned").val();
            price = $("#" + trid + " .price").val();
            net = parseInt(qtysold) * parseFloat(price).toFixed(3);
            discount_percent = parseFloat((d_amount * 100) / net).toFixed(3) || 0.000;
            $("#" + trid + " .discount").val(discount_percent);
            Calculations(trid);
        }

    });


    //ajax request to fetch product data
    $(document).on("change", ".product", function () {

        var id;
        var trid;
        var qtyreturned = 1;
        var price;
        var prePopulate;
        trid = $(this).parents("tr").attr("id");
        id = $(this).val();
        $.ajax({
            url: '/salesreturn/rproduct?id=' + id,
            type: 'GET',
            success: function (data) {
                if (Obj.find_id(id) == undefined) {
                    prePopulate = $.parseJSON(data);
                    Obj.add(trid, prePopulate[0].id, prePopulate[0].barcode);
                    $("#" + trid + " .qtyreturned").val(1);
                    $("#" + trid + " .barcode").val(prePopulate[0].barcode);
                    $("#" + trid + " .price").val(prePopulate[0].sale_price);

                    //calculations function called
                    Calculations(trid);
                    //adding new row
                    $(".dynamic-form-add .add-row").click();
                    // default location selection
                    $(function () {
                        $("#" + trid + " .location option").each(function () {
                            if ($(this).val() == prePopulate[0].location_id) {
                                $(this).attr("selected", "selected");
                            }
                        });
                    });
                    window.scrollBy(0, 60);
                    $("input.barcode:last").focus();
                    $(".product").chosen({search_contains: true, no_results_text: "Oops, nothing found!", width: "100%"});
                    // to disable fields
                    $(".net").prop('readonly', true);
                    $(".product").not(':last').prop("disabled", true).trigger("chosen:updated");
                } else {
                    qtyreturned = $("#" + Obj.find_id(id).row + " .qtyreturned").val();
                    $("#" + Obj.find_id(id).row + " .qtyreturned").val(parseInt(qtyreturned) + 1);
                    //calculations function called
                    Calculations(Obj.find_id(id).row);
                    $(".product:last").val('').trigger("chosen:updated");
                }

            },
            error: function (data) {
                sweetAlert({
                    title: "Oops!",
                    text: "No any product in stock under this product ID!",
                    type: "error"
                });
            }
        });
    });

    // stock select according to location
    $(document).on("change", ".location", function () {
        var id;
        var product_id;
        var present_stock;
        var prePopulate;
        var trid;
        trid = $(this).parents("tr").attr("id");
        product_id = $("#" + trid + " .product").val();
        id = $(this).val();

        $.ajax({
            url: '/sales/present_stock',
            data: {
                'id': id,
                'pid': product_id
            },
            type: 'GET',
            success: function (data) {
                prePopulate = $.parseJSON(data);
                present_stock = prePopulate[0].present_stock;
                $("#" + trid + " .qtypresent").val(present_stock);
            },
            error: function (data) {
                sweetAlert({
                    title: "Oops!",
                    text: "No any data found!",
                    type: "error"
                });
            }
        });
    });

    // customer balance
    $(document).on("change", "#id_customer", function () {
        var balance;
        var paid;
        var net;
        var leg_balance;
        var amount;
        var prePopulate;
        var id = $(this).val();

        $.ajax({
            url: '/salesreturn/sr_balance?id=' + id,
            type: 'GET',
            success: function (data) {
                prePopulate = $.parseJSON(data);
                leg_balance = prePopulate[0].balance;
                $('#id_previous_balance').val(leg_balance);
                amount = $('#id_amount').val();
                paid = $('#id_paid').val();
                net = parseFloat(amount) + parseFloat(leg_balance);
                $('#id_net_amount').val(net);
                balance = net - parseFloat(paid);
                $('#id_balance').val(balance);
                console.log(paid);
            },
            error: function (data) {
                sweetAlert({
                    title: "Oops!",
                    text: "No any data found!",
                    type: "error"
                });
            }
        });
    });

    //ajax request to fetch product data
    $(document).on("change", ".barcode", function () {
        var id;
        var trid;
        var qtyreturned = 1;
        var price;
        var prePopulate;
        trid = $(this).parents("tr").attr("id");
        var barcode = $(this).val();
        $.ajax({
            url: '/salesreturn/rproduct?barcode=' + barcode,
            type: 'GET',
            success: function (data) {
                if (Obj.find_barcode(barcode) == undefined) {
                    prePopulate = $.parseJSON(data);
                    Obj.add(trid, prePopulate[0].id, barcode);
                    $("#" + trid + " .qtyreturned").val(1)
                    $("#" + trid + " .price").val(prePopulate[0].sale_price);
                    $("#" + trid + " .product").val(prePopulate[0].id).trigger("chosen:updated");
                    //calculations function called
                    Calculations(trid);
                    //adding new row
                    $(".dynamic-form-add .add-row").click();
                    // default location selection
                    $(function () {
                        $("#" + trid + " .location option").each(function () {
                            if ($(this).val() == prePopulate[0].location_id) {
                                $(this).attr("selected", "selected");
                            }
                        });
                    });
                    window.scrollBy(0, 60);
                    $("input.barcode:last").focus();
                    $(".product").chosen({search_contains: true, no_results_text: "Oops, nothing found!", width: "100%"});
                    // to disable fields
                    $(".net").prop('readonly', true);
                    $(".product").not(':last').prop("disabled", true).trigger("chosen:updated");
                } else {
                    qtyreturned = $("#" + Obj.find_barcode(barcode).row + " .qtyreturned").val();
                    $("#" + Obj.find_barcode(barcode).row + " .qtyreturned").val(parseInt(qtyreturned) + 1);
                    Calculations(Obj.find_barcode(barcode).row);
                    $(".product:last").val('').trigger("chosen:updated");
                    $(".barcode:last").val('');
                    $(".barcode:last").focus();
                }

            },
            error: function (data) {
                sweetAlert({
                    title: "Oops!",
                    text: "No any product in stock under this barcode!",
                    type: "error"
                });
            }
        });


    });

    // $(document).on("change", ".status", function () {
    //     var trid = $(this).parents("tr").attr("id");
    //     var status = $("#" + trid + " .status option:selected").text();
    //     $("#" + trid + " .location option").each(function (key, value) {
    //
    //         if (value.text == status) {
    //             $("#" + trid + " .location option:selected").text(value.text);
    //             $("#" + trid + " .location option:selected").val(value.val());
    //             }
    //         }
    //     );
    // });


}));

