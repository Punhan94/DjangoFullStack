# Generated by Django 3.2.6 on 2021-09-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_center', '0006_alter_workday_work_day_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
