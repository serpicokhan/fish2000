# Generated by Django 3.2.6 on 2023-08-05 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_personnel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgFile', models.FileField(max_length=200, upload_to='documents/Personel/%Y/%m/%d')),
                ('msgFiledateAdded', models.DateTimeField(auto_now_add=True)),
                ('msgFilePersonel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.personnel', verbose_name='personel_file')),
            ],
            options={
                'db_table': 'personelfile',
            },
        ),
    ]
