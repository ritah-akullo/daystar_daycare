# Generated by Django 5.0.3 on 2024-05-14 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0048_remove_shopform_b_name_sellingform'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellingform',
            name='issued_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='yariapp.babyform'),
        ),
        migrations.AddField(
            model_name='sellingform',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='sellingform',
            name='sold_quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='sellingform',
            name='unit_price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sellingform',
            name='doll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yariapp.shopform'),
        ),
    ]