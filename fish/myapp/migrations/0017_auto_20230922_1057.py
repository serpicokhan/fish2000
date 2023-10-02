# Generated by Django 3.2.6 on 2023-09-22 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_hozurghiab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hozurghiab',
            name='hdate',
            field=models.DateField(default=datetime.date(2023, 9, 22)),
        ),
        migrations.AlterUniqueTogether(
            name='hozurghiab',
            unique_together={('person', 'hdate')},
        ),
    ]
