# Generated by Django 3.2.6 on 2021-10-01 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_center', '0010_alter_workday_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workday',
            name='day_of_week',
            field=models.CharField(choices=[('Bazar ertəsi', 1), ('Çərşənbə axşamı', 2), ('Çərşənbə', 3), ('Cümə axşamı', 4), ('Cümə', 5), ('Şənbə', 6), ('Bazar', 7)], max_length=50),
        ),
    ]
