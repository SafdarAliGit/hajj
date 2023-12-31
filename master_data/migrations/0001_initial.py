# Generated by Django 4.2.7 on 2023-11-29 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Courty Name')),
                ('code', models.CharField(max_length=5, unique=True, verbose_name='Country Code')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='Room Type')),
                ('capacity', models.PositiveIntegerField(verbose_name='Capacity')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Supplier Name')),
                ('country_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country Name')),
                ('currency', models.CharField(choices=[('USD', 'United States Dollar'), ('EUR', 'Euro'), ('JPY', 'Japanese Yen'), ('GBP', 'British Pound Sterling'), ('AUD', 'Australian Dollar'), ('CNY', 'Chinese Yuan'), ('INR', 'Indian Rupee'), ('AED', 'United Arab Emirates Dirham'), ('SAR', 'Saudi Riyal'), ('QAR', 'Qatari Riyal'), ('KWD', 'Kuwaiti Dinar'), ('OMR', 'Omani Rial'), ('BHD', 'Bahraini Dinar'), ('SGD', 'Singapore Dollar'), ('MYR', 'Malaysian Ringgit'), ('THB', 'Thai Baht'), ('IDR', 'Indonesian Rupiah'), ('PHP', 'Philippine Peso'), ('PKR', 'Pakistani Rupee'), ('BDT', 'Bangladeshi Taka'), ('LKR', 'Sri Lankan Rupee')], max_length=3, verbose_name='Currency')),
                ('is_transporters', models.BooleanField(default=False, verbose_name='Transporter')),
                ('is_hotel', models.BooleanField(default=False, verbose_name='Hotel')),
                ('is_hotel_agent', models.BooleanField(default=False, verbose_name='Hotel Agent')),
                ('is_visa_agent', models.BooleanField(default=False, verbose_name='Visa Agent')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact', models.CharField(max_length=15, verbose_name='Contact')),
                ('contact_person', models.CharField(max_length=255, verbose_name='Contact Person')),
                ('address', models.TextField(verbose_name='Address')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='City Name')),
                ('country_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country Name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
