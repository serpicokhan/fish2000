# Generated by Django 3.2.6 on 2022-06-26 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgPririty', models.IntegerField(blank=True, choices=[(1, 'خیلی زیاد'), (2, 'زیاد'), (3, 'متوسط'), (4, 'پایین'), (5, 'خیلی پایین')], null=True, verbose_name='پیامهای سیستمی')),
                ('messageStatus', models.IntegerField(choices=[(3, 'read'), (2, 'unread')], verbose_name='وضعیت')),
                ('sentTime', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True, verbose_name='موضوع')),
                ('Message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20)),
                ('token', models.CharField(blank=True, max_length=20, null=True)),
                ('fullName', models.CharField(max_length=50, verbose_name='مشخصات کامل')),
                ('personalCode', models.CharField(max_length=50, verbose_name='کد پرسنلی')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='نام کاربری')),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True, verbose_name='ایمیل')),
                ('profileImage', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('userStatus', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('userId', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sysusers',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='testuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massage', models.CharField(max_length=50, verbose_name='مشخصات کامل')),
            ],
            options={
                'db_table': 'testuser',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userGroupCode', models.CharField(max_length=50, verbose_name='کد')),
                ('userGroupName', models.CharField(max_length=50, verbose_name='نام')),
                ('userGroupIsPartOF', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.usergroup', verbose_name='زیرمجموعه')),
            ],
            options={
                'db_table': 'usergroup',
            },
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupUserGroups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.usergroup')),
                ('userUserGroups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.sysuser')),
            ],
            options={
                'db_table': 'usergroups',
            },
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userFile', models.FileField(upload_to='documents/')),
                ('userFiledateAdded', models.DateTimeField(auto_now_add=True)),
                ('userFileUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.sysuser')),
            ],
            options={
                'db_table': 'userfile',
            },
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('fromUser', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fromuser1', to='myapp.sysuser', verbose_name='از:')),
                ('toUser', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='touser1', to='myapp.sysuser', verbose_name='به:')),
            ],
            options={
                'db_table': 'msg',
                'ordering': ('date_added',),
            },
        ),
        migrations.CreateModel(
            name='MessageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgFile', models.FileField(max_length=200, upload_to='documents/')),
                ('msgFiledateAdded', models.DateTimeField(auto_now_add=True)),
                ('msgFileworkorder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.message')),
            ],
            options={
                'db_table': 'messagefile',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='fromUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromuser', to='myapp.sysuser', verbose_name='از:'),
        ),
        migrations.AddField(
            model_name='message',
            name='toUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='touser', to='myapp.sysuser', verbose_name='به:'),
        ),
    ]