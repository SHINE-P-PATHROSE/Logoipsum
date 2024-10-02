# Generated by Django 5.1.1 on 2024-10-02 05:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Author Name')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('action_status', models.BooleanField(default=True, verbose_name='Action Status')),
            ],
            options={
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('author_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('action', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
