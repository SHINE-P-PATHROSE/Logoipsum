# Generated by Django 5.1.1 on 2024-09-27 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0002_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
