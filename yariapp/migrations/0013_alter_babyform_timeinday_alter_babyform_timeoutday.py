# Generated by Django 5.0.3 on 2024-04-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0012_alter_babyform_timeinday_alter_babyform_timeoutday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babyform',
            name='timeInDay',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='babyform',
            name='timeOutDay',
            field=models.DateTimeField(),
        ),
    ]
