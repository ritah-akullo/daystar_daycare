# Generated by Django 5.0.3 on 2024-05-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0021_alter_proform_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ondutyform',
            name='telephone_no',
            field=models.DateField(blank=True, null=True),
        ),
    ]
