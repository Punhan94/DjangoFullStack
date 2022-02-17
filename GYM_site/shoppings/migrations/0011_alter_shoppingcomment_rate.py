# Generated by Django 3.2.6 on 2021-09-14 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppings', '0010_alter_shoppingcomment_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcomment',
            name='rate',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]