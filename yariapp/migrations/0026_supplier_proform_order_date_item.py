# Generated by Django 5.0.3 on 2024-05-06 08:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0025_alter_arrivalform_timeinday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='proform',
            name='order_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField(default=0)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='yariapp.supplier')),
            ],
        ),
    ]
