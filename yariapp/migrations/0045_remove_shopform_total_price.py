# Generated by Django 5.0.3 on 2024-05-14 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0044_remove_babyform_baby_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopform',
            name='total_price',
        ),
    ]
