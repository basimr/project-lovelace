# Generated by Django 2.1.5 on 2019-07-16 12:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_reorder-problems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='order_id',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
