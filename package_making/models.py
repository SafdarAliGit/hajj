from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from locations.models import Country, City
from rooms.models import RoomType
from supplier.models import Supplier


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Hotel(TimeStampModel):
    name = models.CharField(max_length=255, null=False, verbose_name='Hotel Name')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Supplier Name')
    supplier_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Supplier Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')
    country_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Country Name')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='City')
    city_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='City Name')
    contact_person = models.CharField(max_length=255, verbose_name='Contact Person')
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')
    address = models.TextField(verbose_name='Address')
    email = models.EmailField(verbose_name='Email')
    wifi_included = models.BooleanField(default=False, verbose_name='Wifi Included')
    restaurant_included = models.BooleanField(default=False, verbose_name='Restaurant Included')

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.name


class HotelPurchasePrice(TimeStampModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Hotel')
    hotel_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Hotel Name')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name='Room Type')
    room_type_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Room Type Name')
    rate_valid_from = models.DateField(verbose_name='Rate Valid From')
    rate_valid_till = models.DateField(verbose_name='Rate Valid Till')
    meal_choices = [
        ('RO', 'Room Only'),
        ('BB', 'Bed & Breakfast'),
        ('HB', 'Half Board'),
        ('FB', 'Full Board'),
    ]

    CURRENCY_CHOICES = [
        ('SAR', 'Saudi Riyal'),
        ('PKR', 'Pakistani Rupee'),
    ]
    meal = models.CharField(max_length=2, choices=meal_choices, verbose_name='Meal')
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Purchase Rate')
    sale_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Sale Rate')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name='Currency')


@receiver(pre_save, sender=HotelPurchasePrice)
def set_hotel_name(sender, instance, **kwargs):
    if instance.hotel:
        instance.hotel_name = instance.hotel.name
    else:
        instance.hotel_name = None

    if instance.room_type:
        instance.room_type_name = instance.room_type.name
    else:
        instance.room_type_name = None  # Set to a default value or handle it according to your logic


@receiver(pre_save, sender=Hotel)
def set_country_and_city_name(sender, instance, **kwargs):
    if instance.country:
        instance.country_name = instance.country.name
    else:
        instance.country_name = None

    if instance.city:
        instance.city_name = instance.city.name
    else:
        instance.city_name = None

    if instance.supplier:
        instance.supplier_name = instance.supplier.name
    else:
        instance.supplier_name = None


class Package(TimeStampModel):
    PACKAGE_TYPES = [
        ('Hajj', 'Hajj'),
        ('Tour', 'Tour'),
        ('Umrah', 'Umrah'),
    ]

    MAKTAB_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    name = models.CharField(max_length=100, verbose_name='Package Name', unique=True)
    package_type = models.CharField(max_length=10, choices=PACKAGE_TYPES, verbose_name='Package Type')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')
    country_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Country Name')
    country_code = models.CharField(max_length=10, verbose_name='Country Code')
    package_days = models.IntegerField(verbose_name='Package Days')
    maktab = models.CharField(max_length=1, choices=MAKTAB_CHOICES, verbose_name='Maktab')
    package_sale_price_sar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Package Sale Price(SAR)')
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Exchange Rate')
    package_sale_price_pkr = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Package Sale Price(PKR)')
    terms_and_conditions = models.TextField(verbose_name='Terms and Conditions')



    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.name


class PackageHotelItem(TimeStampModel):
    MEAL_CHOICES = [
        ('RO', 'Room Only'),
        ('BB', 'Bed & Breakfast'),
        ('HB', 'Half Board'),
        ('FB', 'Full Board'),
    ]

    CURRENCY_CHOICES = [
        ('SAR', 'Saudi Riyal'),
        ('PKR', 'Pakistani Rupee'),

    ]

    package = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name='Package')
    package_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Package Name')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='City')
    city_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='City Name')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Hotel')
    hotel_name= models.CharField(max_length=100, blank=True, null=True, verbose_name='Hotel Name')
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name='Room Type')
    room_type_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Room Type Name')
    check_in_date = models.DateField(verbose_name='Check In Date')
    check_out_date = models.DateField(verbose_name='Check Out Date')
    meal = models.CharField(max_length=2, choices=MEAL_CHOICES, verbose_name='Meal')
    nights = models.IntegerField(verbose_name='Nights')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cost')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, verbose_name='Currency')

    class Meta:
        verbose_name = 'Package Hotel Item'
        verbose_name_plural = 'Package Hotel Items'

    def __str__(self):
        return f"{self.package.name} - {self.hotel.name}"


@receiver(pre_save, sender=Package)
def set_package_fields(sender, instance, **kwargs):
    if instance.country:
        instance.country_name = instance.country.name
    else:
        instance.country_name = None

    if instance.country:
        instance.country_code = instance.country.code
    else:
        instance.country_code = None


@receiver(pre_save, sender=PackageHotelItem)
def set_package_hotel_item_fields(sender, instance, **kwargs):
    if instance.package:
        instance.package_name = instance.package.name
    else:
        instance.package_name = None

    if instance.city:
        instance.city_name = instance.city.name
    else:
        instance.city_name = None

    if instance.hotel:
        instance.hotel_name = instance.hotel.name
    else:
        instance.hotel_name = None

    if instance.room_type:
        instance.room_type_name = instance.room_type.name
    else:
        instance.room_type_name = None
