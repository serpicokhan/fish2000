# Generated by Django 3.2.6 on 2022-06-29 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_fish_mande_morakhasi'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='shekayat',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='مانده مرخصی'),
        ),
    ]