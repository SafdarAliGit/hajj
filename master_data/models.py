from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RoomType(TimeStampModel):
    name = models.CharField(max_length=150, verbose_name='Room Type')
    capacity = models.PositiveIntegerField(verbose_name='Capacity')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name


# ==============
class Country(TimeStampModel):
    name = models.CharField(max_length=100, null=False, verbose_name='Courty Name', unique=True)
    code = models.CharField(max_length=5, null=False, verbose_name='Country Code', unique=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(TimeStampModel):
    name = models.CharField(max_length=100, verbose_name='City Name', unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')
    country_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Country Name')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


@receiver(pre_save, sender=City)
def set_country_name(sender, instance, **kwargs):
    if instance.country:
        instance.country_name = instance.country.name
    else:
        instance.country_name = None

# ==============
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Supplier(TimeStampModel):

    CURRENCIES = [
        ('USD', 'United States Dollar'),
        ('EUR', 'Euro'),
        ('JPY', 'Japanese Yen'),
        ('GBP', 'British Pound Sterling'),
        ('AUD', 'Australian Dollar'),
        ('CNY', 'Chinese Yuan'),
        ('INR', 'Indian Rupee'),
        ('AED', 'United Arab Emirates Dirham'),
        ('SAR', 'Saudi Riyal'),
        ('QAR', 'Qatari Riyal'),
        ('KWD', 'Kuwaiti Dinar'),
        ('OMR', 'Omani Rial'),
        ('BHD', 'Bahraini Dinar'),
        ('SGD', 'Singapore Dollar'),
        ('MYR', 'Malaysian Ringgit'),
        ('THB', 'Thai Baht'),
        ('IDR', 'Indonesian Rupiah'),
        ('PHP', 'Philippine Peso'),
        ('PKR', 'Pakistani Rupee'),
        ('BDT', 'Bangladeshi Taka'),
        ('LKR', 'Sri Lankan Rupee'),
    ]

    name = models.CharField(max_length=255, verbose_name='Supplier Name')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country')
    country_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Country Name')
    currency = models.CharField(max_length=3, choices=CURRENCIES, verbose_name='Currency')
    is_transporters = models.BooleanField(default=False, verbose_name='Transporter')
    is_hotel = models.BooleanField(default=False, verbose_name='Hotel')
    is_hotel_agent = models.BooleanField(default=False, verbose_name='Hotel Agent')
    is_visa_agent = models.BooleanField(default=False, verbose_name='Visa Agent')
    email = models.EmailField(verbose_name='Email')
    contact = models.CharField(max_length=15, verbose_name='Contact')
    contact_person = models.CharField(max_length=255, verbose_name='Contact Person')
    address = models.TextField(verbose_name='Address')
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Supplier)
def set_country_name(sender, instance, **kwargs):
    if instance.country:
        instance.country_name = instance.country.name
    else:
        instance.country_name = None

# ==============
