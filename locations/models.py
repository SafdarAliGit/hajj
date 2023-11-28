from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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
