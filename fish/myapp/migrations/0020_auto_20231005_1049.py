# Generated by Django 3.2.6 on 2023-10-05 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20230926_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hozurghiab',
            name='hdate',
            field=models.DateField(default=datetime.date(2023, 10, 5)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='Pid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
