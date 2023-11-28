from django.contrib import admin

from package_making.forms import PackageHotelItemForm
from package_making.models import Hotel, HotelPurchasePrice, PackageHotelItem, Package


class HotelPurchasePriceInline(admin.TabularInline):  # or admin.StackedInline
    exclude = ('hotel_name','room_type_name',)
    model = HotelPurchasePrice
    extra = 1  # Number of empty forms to display for adding new records


class HotelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (tuple(['name', 'supplier', 'country', 'city', 'contact_person','phone_number','email' ]),
                       'address', tuple(['wifi_included','restaurant_included']),),
        }),

    )
    list_display = ('name', 'supplier', 'country', 'city',)
    filter = ('name', 'supplier', 'country', 'city',)
    inlines = [HotelPurchasePriceInline]
    exclude = ('supplier_name', 'country_name', 'city_name',)


class PackageHotelItemInline(admin.TabularInline):  # or admin.StackedInline
    exclude = ('package_name','city_name','room_type_name','hotel_name',)
    model = PackageHotelItem
    form = PackageHotelItemForm
    extra = 1  # Number of empty forms to display for adding new records


class PackageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (tuple(['name', 'package_type','maktab', 'country', 'package_days',]),tuple(['package_sale_price_sar', 'exchange_rate', 'package_sale_price_pkr']),'terms_and_conditions'),
        }),

    )
    class Media:
        js = ["admin/js/jquery.init.js","admin/js/admin_package.js"]

    list_display = ('name', 'package_type', 'country', 'package_days','maktab',)
    filter = ('name', 'package_type', 'country', 'package_days','maktab',)
    inlines = [PackageHotelItemInline]
    exclude = ('country_name','country_code',)






admin.site.register(Hotel, HotelAdmin)
admin.site.register(Package, PackageAdmin)
