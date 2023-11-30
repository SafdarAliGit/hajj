// function updateTotalCostRow() {
//     // calculations of sum of cost
//     var total_cost = 0;
//     $(".cost").each(function () {
//         var cost = parseFloat($(this).val());
//             total_cost += cost || 0;
//     });
//
//     var newRowContent = `${total_cost}`;
//     var newRow = `<tr class="total_cost" style="font-weight: bold;font-size: 1em;background-color: #FFFFCC;"><td>TOTAL:</td><td colspan="7"></td><td>${newRowContent}</td><td colspan="2"></td></tr>`;
//
//     if ($('.total_cost').length) {
//         $('.total_cost').replaceWith(newRow);
//     } else {
//         $('tr:has(td.field-meal):last').after(newRow);
//     }
// }


$(document).ready(function () {
    $(document).on("change", "#id_package", function () {
        var package_id = $(this).val();

        if (package_id) {
            $.ajax({
                url: `/hajj_application/get_package?package_id=${package_id}`,
                type: 'GET',
                success: function (data) {
                    if (data.success && data.package) {
                        console.log(data.package);
                    } else {
                        console.log('no data');
                    }
                },
                error: function (data) {
                    alert('An error occurred.');
                }
            });
        } else {
            alert("Package is required");
        }

    });
});