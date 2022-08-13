# Generated by Django 4.0.6 on 2022-08-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='rentel_price_day',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]