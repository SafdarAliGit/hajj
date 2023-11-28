(function ($) {
    $(document).on("change", ".meal", function () {
        var row_num = $(this).parents("tr").attr("id").split("-")[1];
        var country_id = $(`#id_country`).val();
        var city_id = $(`#id_packagehotelitem_set-${row_num}-city`).val();
        var hotel_id = $(`#id_packagehotelitem_set-${row_num}-hotel`).val();
        var room_type_id = $(`#id_packagehotelitem_set-${row_num}-room_type`).val();
        var meal = $(this).val();

        if (city_id && hotel_id && room_type_id && country_id && meal) {
            $.ajax({
                url: `/get_hotel_price?country_id=${country_id}&city_id=${city_id}&hotel_id=${hotel_id}&room_type_id=${room_type_id}&meal=${meal}`,
                type: 'GET',
                success: function (data) {
                    if (data.success && data.prices) {
                        $(`#id_packagehotelitem_set-${row_num}-cost`).val(data.prices.sale_rate);
                        $(`#id_packagehotelitem_set-${row_num}-check_in_date`).val(data.prices.rate_valid_from);
                        $(`#id_packagehotelitem_set-${row_num}-check_out_date`).val(data.prices.rate_valid_till);
                        $(`#id_packagehotelitem_set-${row_num}-nights`).val(data.prices.nights);
                        $(`#id_packagehotelitem_set-${row_num}-cost`).val(data.prices.cost);
                        $(`#id_packagehotelitem_set-${row_num}-currency`).val(data.prices.currency);
                    } else {
                        $(`#id_packagehotelitem_set-${row_num}-cost`).val(null);
                        $(`#id_packagehotelitem_set-${row_num}-check_in_date`).val(null);
                        $(`#id_packagehotelitem_set-${row_num}-check_out_date`).val(null);
                        $(`#id_packagehotelitem_set-${row_num}-nights`).val(null);
                        $(`#id_packagehotelitem_set-${row_num}-cost`).val(null);
                        $(`#id_packagehotelitem_set-${row_num}-currency`).val(data.prices.currency);
                    }
                },
                error: function (data) {
                    alert('An error occurred.');
                }
            });
        } else {
            alert("City, Hotel, Country, Check-in_date, Check-out_date and Room Type are required");
        }

    });
})
(django.jQuery);


