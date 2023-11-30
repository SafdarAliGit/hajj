# Generated by Django 4.2.7 on 2023-11-29 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package_making', '0001_initial'),
        ('hajj_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hajjapplication',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='package_making.package', verbose_name='Package'),
        ),
        migrations.AddField(
            model_name='hajjapplication',
            name='package_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Package Name'),
        ),
    ]