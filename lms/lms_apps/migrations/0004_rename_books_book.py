# Generated by Django 4.0.6 on 2022-08-02 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_apps', '0003_alter_books_price_alter_books_rentel_price_day'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='books',
            new_name='book',
        ),
    ]
