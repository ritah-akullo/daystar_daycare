# Generated by Django 5.0.3 on 2024-05-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0028_remove_payform_c_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentform',
            name='c_payment',
        ),
        migrations.AddField(
            model_name='paymentform',
            name='Baby_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]