# Generated by Django 3.2.6 on 2021-09-30 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20210930_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='user',
        ),
    ]
