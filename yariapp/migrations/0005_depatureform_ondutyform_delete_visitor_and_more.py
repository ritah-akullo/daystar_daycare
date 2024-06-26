# Generated by Django 5.0.3 on 2024-04-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yariapp', '0004_payment_paid_by_alter_sittersform_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depatureform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(blank=True, max_length=50)),
                ('parent_name', models.CharField(blank=True, max_length=50)),
                ('timeInDay', models.DateField(blank=True, null=True)),
                ('timeOutDay', models.DateField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('person_pickingup', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OnDutyform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('period', models.DateTimeField(auto_now_add=True)),
                ('baby_assigned_to', models.CharField(blank=True, max_length=200, null=True)),
                ('telephone_no', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
        migrations.AlterField(
            model_name='categorystay',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
