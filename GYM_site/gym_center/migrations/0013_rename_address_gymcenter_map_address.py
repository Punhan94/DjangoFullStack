# Generated by Django 3.2.6 on 2021-10-02 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_center', '0012_gymcenter_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gymcenter',
            old_name='address',
            new_name='map_address',
        ),
    ]
