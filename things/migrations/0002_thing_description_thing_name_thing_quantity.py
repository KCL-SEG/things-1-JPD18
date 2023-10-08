# Generated by Django 4.2.6 on 2023-10-08 21:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='thing',
            name='name',
            field=models.CharField(default='guy', max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='thing',
            name='quantity',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
