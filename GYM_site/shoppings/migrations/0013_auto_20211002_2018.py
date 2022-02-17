# Generated by Django 3.2.6 on 2021-10-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppings', '0012_rename_crated_date_shoppingcomment_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='shoppings.Category'),
        ),
    ]
