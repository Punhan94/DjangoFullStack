# Generated by Django 3.2.6 on 2021-09-17 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_center', '0007_alter_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymcenter',
            name='center_images',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
