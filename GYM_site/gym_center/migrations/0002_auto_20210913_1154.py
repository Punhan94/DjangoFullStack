# Generated by Django 3.2.6 on 2021-09-13 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_center', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='product',
            new_name='gym_center',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='product',
            new_name='gym_center',
        ),
    ]
