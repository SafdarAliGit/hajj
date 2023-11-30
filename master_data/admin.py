from django.contrib import admin

from master_data.models import Country, City, Supplier, RoomType


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    exclude = ('country_name',)
    list_filter = ('country',)


@admin.register(Supplier)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    exclude = ('country_name',)
    list_filter = ('name', 'country',)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity',)
