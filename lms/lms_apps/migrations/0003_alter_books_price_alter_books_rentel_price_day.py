# Generated by Django 4.0.6 on 2022-08-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_apps', '0002_alter_books_price_alter_books_rentel_price_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='rentel_price_day',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]