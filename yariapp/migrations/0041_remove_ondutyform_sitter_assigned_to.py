# Generated by Django 5.0.3 on 2024-05-13 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0040_rename_baby_name_arrivalform_b_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ondutyform',
            name='sitter_assigned_to',
        ),
    ]