# Generated by Django 3.2.6 on 2023-09-26 06:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_rename_ghayeb_hozurghiab_hozur'),
    ]

    operations = [
        migrations.AddField(
            model_name='hozurghiab',
            name='registerd_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to='myapp.sysuser'),
        ),
        migrations.AlterField(
            model_name='hozurghiab',
            name='hdate',
            field=models.DateField(default=datetime.date(2023, 9, 26)),
        ),
    ]
