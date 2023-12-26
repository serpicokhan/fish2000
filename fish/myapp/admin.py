from django.contrib import admin
from myapp.models import *
admin.site.register(SysUser)
admin.site.register(Asset)
admin.site.register(AssetUser)

# Register your models here.
