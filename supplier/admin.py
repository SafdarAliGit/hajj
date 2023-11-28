from django.contrib import admin

from supplier.models import Supplier


@admin.register(Supplier)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    exclude = ('country_name',)
    list_filter = ('name', 'country',)

