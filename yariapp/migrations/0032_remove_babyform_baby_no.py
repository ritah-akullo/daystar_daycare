# Generated by Django 5.0.3 on 2024-05-08 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0031_alter_babyform_baby_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babyform',
            name='baby_no',
        ),
    ]
