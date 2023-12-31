# Generated by Django 3.2.6 on 2023-09-18 10:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20230918_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='HozurGhiab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incom_time', models.TimeField()),
                ('outcome_time', models.TimeField()),
                ('hdate', models.DateField(default=datetime.date(2023, 9, 18))),
                ('registerd_date', models.DateTimeField(auto_now_add=True)),
                ('ghayeb', models.BooleanField(default=False)),
                ('estehghaghi', models.BooleanField(default=False)),
                ('estelaji', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_hozur', to='myapp.personnel')),
            ],
            options={
                'db_table': 'hozurghiab',
            },
        ),
    ]
