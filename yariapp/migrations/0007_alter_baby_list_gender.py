# Generated by Django 5.0.3 on 2024-04-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0006_arrivalform_baby_list_remove_sittersform_timein_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby_list',
            name='Gender',
            field=models.CharField(max_length=50, null=True),
        ),
    ]