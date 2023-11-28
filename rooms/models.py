from django.db import models


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
