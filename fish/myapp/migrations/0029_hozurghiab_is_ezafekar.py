# Generated by Django 3.2.6 on 2023-10-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_remove_hozurghiab_is_ezafekar'),
    ]

    operations = [
        migrations.AddField(
            model_name='hozurghiab',
            name='is_ezafekar',
            field=models.BooleanField(default=False),
        ),
    ]
