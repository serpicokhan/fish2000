# Generated by Django 3.2.6 on 2023-09-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_personelfile_msgfiledtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='personelfile',
            name='msgFileName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personnel',
            name='Shift',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
