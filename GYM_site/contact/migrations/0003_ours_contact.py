# Generated by Django 3.2.6 on 2021-09-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ours_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ours_location', models.CharField(blank=True, max_length=100)),
                ('ours_email', models.EmailField(blank=True, max_length=254)),
                ('ours_mobil_telephone', models.CharField(blank=True, max_length=50)),
                ('ours_office_phone', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]