# Generated by Django 3.2.6 on 2023-09-18 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_personnel_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetTypes', models.IntegerField(blank=True, choices=[(1, 'مکان'), (2, 'ماشین  آلات'), (3, 'ابزارآلات')], null=True, verbose_name='نوع دارایی')),
                ('assetName', models.CharField(max_length=100, verbose_name='مشخصات')),
                ('assetDescription', models.CharField(blank=True, max_length=100, null=True, verbose_name='توضیحات')),
                ('assetCode', models.CharField(blank=True, max_length=50, null=True, verbose_name='کد')),
                ('assetAddress', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس')),
                ('assetCity', models.CharField(blank=True, max_length=50, null=True, verbose_name='شهر')),
                ('assetState', models.CharField(blank=True, max_length=50, null=True, verbose_name='استان')),
                ('assetZipcode', models.CharField(blank=True, max_length=50, null=True, verbose_name='کد پستی')),
                ('assetCountry', models.CharField(blank=True, max_length=100, null=True, verbose_name='کشور')),
                ('assetAccount', models.CharField(blank=True, max_length=100, null=True, verbose_name='حساب')),
                ('assetChargeDepartment', models.CharField(blank=True, max_length=100, null=True, verbose_name='دپارتمان مسوول')),
                ('assetNotes', models.CharField(blank=True, max_length=100, null=True, verbose_name='یادداشت')),
                ('assetBarcode', models.IntegerField(blank=True, null=True, verbose_name='بارکد')),
                ('assetHasPartOf', models.BooleanField(default=False)),
                ('assetAisel', models.IntegerField(blank=True, null=True, verbose_name='راهرو')),
                ('assetRow', models.IntegerField(blank=True, null=True, verbose_name='ردیف')),
                ('assetBin', models.IntegerField(blank=True, null=True, verbose_name='Bin')),
                ('assetManufacture', models.CharField(blank=True, max_length=50, null=True, verbose_name='سازنده')),
                ('assetModel', models.CharField(blank=True, max_length=50, null=True, verbose_name='مدل')),
                ('assetSerialNumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره سریال')),
                ('assetStatus', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('assetIsStock', models.BooleanField(default=False, verbose_name='انبار')),
            ],
            options={
                'db_table': 'assets',
            },
        ),
        migrations.CreateModel(
            name='BatchMeterGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchMeterGroupName', models.CharField(max_length=50, unique=True, verbose_name='نام گروه اندازه گیری')),
            ],
            options={
                'db_table': 'batchmetergroup',
            },
        ),
        migrations.CreateModel(
            name='BOMGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BOMGroupName', models.CharField(max_length=50, unique=True, verbose_name='نام گروه BOM')),
            ],
            options={
                'db_table': 'bomgroup',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('code', models.CharField(max_length=50, verbose_name='کد')),
                ('primaryContact', models.CharField(blank=True, max_length=100, null=True, verbose_name='مشخصات تماس')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='تلفن')),
                ('phone2', models.CharField(blank=True, max_length=50, null=True, verbose_name='تلفن 2')),
                ('fax', models.CharField(blank=True, max_length=50, null=True, verbose_name='فکس')),
                ('webSite', models.CharField(blank=True, max_length=50, null=True, verbose_name='سایت')),
                ('primaryEmail', models.CharField(blank=True, max_length=50, null=True, verbose_name='ایمیل اصلی')),
                ('secondyEmail', models.CharField(blank=True, max_length=50, null=True, verbose_name='ایمیل 2')),
                ('primaryCurrency', models.CharField(blank=True, max_length=50, null=True, verbose_name='واحد پول')),
                ('notes', models.CharField(blank=True, max_length=100, null=True, verbose_name='یادداشت')),
                ('isSupplier', models.BooleanField(default=False, verbose_name='تامین کننده')),
                ('insManufacturer', models.BooleanField(default=False, verbose_name='سازننده')),
                ('isServiceProvider', models.BooleanField(default=False, verbose_name='سرویس پروایدر')),
                ('isOwner', models.BooleanField(default=False, verbose_name='مالک')),
                ('isCustomer', models.BooleanField(default=False, verbose_name='مشتری')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='شهر')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='استان')),
                ('postalCode', models.CharField(blank=True, max_length=50, null=True, verbose_name='کد پستی')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='کشور')),
            ],
            options={
                'db_table': 'business',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partName', models.CharField(max_length=100, verbose_name='مشخصات')),
                ('partDescription', models.CharField(max_length=100, verbose_name='توضیحات')),
                ('partCode', models.CharField(max_length=50, verbose_name='کد')),
                ('partMake', models.CharField(blank=True, max_length=100, null=True, verbose_name='ساخته شده توسط')),
                ('partModel', models.CharField(blank=True, max_length=50, null=True, verbose_name='مدل')),
                ('partLastPrice', models.FloatField(blank=True, default=0, null=True, verbose_name='آخرین قیمت')),
                ('partAccount', models.CharField(blank=True, max_length=100, null=True, verbose_name='حساب')),
                ('partChargeDepartment', models.CharField(blank=True, max_length=100, null=True, verbose_name='دپارتمان مسوول')),
                ('partNotes', models.CharField(blank=True, max_length=100, null=True, verbose_name='یادداشت')),
                ('partBarcode', models.IntegerField(blank=True, null=True, verbose_name='بارکد')),
                ('partInventoryCode', models.CharField(blank=True, max_length=50, null=True, verbose_name='کد قفسه')),
            ],
            options={
                'db_table': 'parts',
            },
        ),
        migrations.AddField(
            model_name='personnel',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sarshift', to='myapp.sysuser'),
        ),
        migrations.CreateModel(
            name='PartUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PartUserPartId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.part', verbose_name='قطعه')),
                ('PartUserUserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.sysuser', verbose_name='کاربر ')),
            ],
            options={
                'db_table': 'partuser',
            },
        ),
        migrations.CreateModel(
            name='PartFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partFile', models.FileField(max_length=200, upload_to='documents/')),
                ('partFiledateAdded', models.DateTimeField(auto_now_add=True)),
                ('partFilePartId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.part')),
            ],
            options={
                'db_table': 'partfile',
            },
        ),
        migrations.CreateModel(
            name='PartCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='کد')),
                ('description', models.CharField(max_length=50, verbose_name='توضیحات')),
                ('priority', models.IntegerField(null=True, verbose_name='اولویت')),
                ('isPartOf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.partcategory', verbose_name='زیر مجموعه')),
            ],
            options={
                'db_table': 'partcategory',
            },
        ),
        migrations.AddField(
            model_name='part',
            name='partCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dasdadassa', to='myapp.partcategory', verbose_name='دسته بندی'),
        ),
        migrations.CreateModel(
            name='BusinessUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.sysuser', verbose_name='پرسنل')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.part', verbose_name='نام قطعه')),
            ],
            options={
                'db_table': 'businessuser',
            },
        ),
        migrations.CreateModel(
            name='BusinessPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessPartBusinessType', models.IntegerField(blank=True, choices=[(0, 'تامین کننده'), (1, 'سارننده'), (2, 'خدماتی'), (3, 'مالک'), (4, 'مشتری')], null=True, verbose_name='نوع کسب و کار')),
                ('businessPartSupplierPartNumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='پارت نامبر تامین کننده')),
                ('businessPartCatalog', models.CharField(blank=True, max_length=100, null=True, verbose_name='دسته بندی')),
                ('businessPartisDefault', models.BooleanField(default=False, verbose_name='تامین کننده مورد علاقه')),
                ('businessPartVendorPrice', models.FloatField(blank=True, null=True, verbose_name='قیمت تامین کننده')),
                ('BusinessPartPart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.part', verbose_name='نام قطعه')),
                ('businessPartBusiness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.business', verbose_name='تامین کننده')),
            ],
            options={
                'db_table': 'businesspart',
            },
        ),
        migrations.CreateModel(
            name='BusinessFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessFile', models.FileField(upload_to='documents/')),
                ('businessFiledateAdded', models.DateTimeField(auto_now_add=True)),
                ('businessFileBusinessId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.business')),
            ],
            options={
                'db_table': 'businessfiles',
            },
        ),
        migrations.CreateModel(
            name='BusinessAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessAssetBusinessType', models.IntegerField(blank=True, choices=[(0, 'تامین کننده'), (1, 'سارننده'), (2, 'خدماتی'), (3, 'مالک'), (4, 'مشتری')], null=True, verbose_name='نوع کسب و کار')),
                ('businessAssetSupplierPartNumber', models.CharField(blank=True, max_length=100, null=True, verbose_name='پارت نامبر تامین کننده')),
                ('businessAssetCatalog', models.CharField(blank=True, max_length=100, null=True, verbose_name='دسته بندی')),
                ('businessAssetisDefault', models.BooleanField(default=False, verbose_name='تامین کننده مورد علاقه')),
                ('businessAssetVendorPrice', models.FloatField(blank=True, null=True, verbose_name='قیمت تامین کننده')),
                ('BusinessAssetAsset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset', verbose_name='نام دارایی')),
                ('businessAssetBusiness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.business', verbose_name='کسب و کار')),
            ],
            options={
                'db_table': 'businessasset',
            },
        ),
        migrations.CreateModel(
            name='AssetUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssetUserAssetId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset', verbose_name='دارایی')),
                ('AssetUserUserId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.sysuser', verbose_name='کاربر ')),
            ],
            options={
                'db_table': 'assetuser',
            },
        ),
        migrations.CreateModel(
            name='AssetPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetPartQnty', models.IntegerField(blank=True, null=True, verbose_name='تعداد')),
                ('assetPartDescription', models.CharField(blank=True, max_length=50, null=True, verbose_name='توضیح')),
                ('assetPartAssetid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset', verbose_name='نام دارایی')),
                ('assetPartBOMGroupName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.bomgroup', verbose_name='گروه')),
                ('assetPartPid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.part', verbose_name='نام قطعه')),
            ],
            options={
                'db_table': 'assetpart',
            },
        ),
        migrations.CreateModel(
            name='AssetFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetFile', models.FileField(max_length=200, upload_to='documents/')),
                ('assetFiledateAdded', models.DateTimeField(auto_now_add=True)),
                ('assetFileAssetId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.asset')),
            ],
            options={
                'db_table': 'assetfile',
            },
        ),
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('code', models.CharField(max_length=50, verbose_name='کد')),
                ('description', models.CharField(max_length=50, verbose_name='توضیحات')),
                ('priority', models.IntegerField(null=True, verbose_name='اولویت')),
                ('isPartOf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.assetcategory', verbose_name='زیر مجموعه')),
            ],
            options={
                'db_table': 'assetcategory',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='assetCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.assetcategory', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='asset',
            name='assetIsLocatedAt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='myapp.asset', verbose_name='مکان'),
        ),
        migrations.AddField(
            model_name='asset',
            name='assetIsPartOf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.asset', verbose_name='زیر مجموعه'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='saloon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saloon', to='myapp.asset'),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtyOnHand', models.IntegerField(blank=True, null=True, verbose_name='موجودی')),
                ('minQty', models.IntegerField(blank=True, null=True, verbose_name='حداقل موجودی')),
                ('aisle', models.IntegerField(blank=True, null=True, verbose_name='راهرو')),
                ('row', models.IntegerField(blank=True, null=True, verbose_name='ردیف')),
                ('bin', models.IntegerField(blank=True, null=True, verbose_name='قفسه')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.asset', verbose_name='مکان')),
                ('stockItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.part', verbose_name='نام قطعه')),
            ],
            options={
                'db_table': 'stocks',
                'unique_together': {('stockItem', 'location')},
            },
        ),
        migrations.CreateModel(
            name='BOMGroupPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BOMGroupPartQnty', models.IntegerField(blank=True, null=True, verbose_name='تعداد')),
                ('BOMGroupPartBOMGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.bomgroup', verbose_name='گروه')),
                ('BOMGroupPartPart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.part', verbose_name='قطعه')),
            ],
            options={
                'db_table': 'bomgrouppart',
                'unique_together': {('BOMGroupPartPart', 'BOMGroupPartBOMGroup')},
            },
        ),
    ]
