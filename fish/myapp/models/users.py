#python manage.py makemigrations
#After that you just have to run migrate command for syncing database .

#python manage.py migrate --run-syncdb
from django.db import models
from datetime import datetime
import os
from django.contrib.auth.models import User
import jdatetime
from django.utils.timezone import now
# from cmms.models.Asset import *
class testuser(models.Model):
    # password=models.CharField(max_length=20)
    massage=models.CharField("مشخصات کامل",max_length = 50)
    class Meta:
        db_table="testuser"


class SysUser(models.Model):
    def __str__(self):
        return "{}".format(self.fullName)
    def get_userStatus(self):
                 if(self.userStatus==True):
                     return "<span class='badge badge-success'><span class='mr-1 fa fa-check'></span>کامل شد</span>"
                 else:
                     return "<span class='badge badge-success'><span class='mr-1 fa fa-check'></span>کامل شد</span>"
    def getName(self):

        xxxx=UserGroups.objects.filter(userUserGroups=self.id)
        st=[]
        for i in xxxx:
            st.append(i.groupUserGroups)
        # print(''.join(str(e) for e in st))
        return '<br/>'.join(str(e) for e in st)


    Dashboard=1
    WorkOrderAssignedToMe=2
    MessageCenterInbox=3
    WorkOrders=4
    Location=(
        (Dashboard,'داشبورد'),
        (WorkOrderAssignedToMe,'درخواستهای انتسابی به من'),
        (MessageCenterInbox,'صندوق ورودی پیامها'),
        (WorkOrders,'درخواست'),
    )
    userId = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    password=models.CharField(max_length=20)
    token=models.CharField(max_length=20,null=True,blank=True)
    fullName=models.CharField("مشخصات کامل",max_length = 50)
    personalCode=models.CharField("کد پرسنلی",max_length = 50)
    title=models.CharField("نام کاربری",max_length = 50,null=True,blank=True)
    email=models.EmailField("ایمیل",max_length=70,blank=True, null= True, unique= True)
    profileImage = models.ImageField(upload_to='images/',default=None,blank=True)

    userStatus=models.BooleanField("وضعیت",default=True)

    class Meta:
        db_table="sysusers"
        ordering = ['title']



class UserGroup(models.Model):
    def __str__(self):
        if(self.userUserLocation):
            return "{}:{}".format(self.userGroupName,self.userUserLocation)
        else:
            return "{}".format(self.userGroupName)

    userGroupCode=models.CharField("کد",max_length=50)
    userGroupName=models.CharField("نام",max_length=50)

    userGroupIsPartOF=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,verbose_name='زیرمجموعه')

    class Meta:
        db_table="usergroup"

class UserGroups(models.Model):


    userUserGroups=models.ForeignKey(SysUser,on_delete=models.CASCADE,blank=True,null=True)
    groupUserGroups=models.ForeignKey(UserGroup,on_delete=models.CASCADE,blank=True,null=True)
    class Meta:
        db_table="usergroups"
class UserFile(models.Model):
    def get_ext(self):
        v=os.path.splitext(self.userFile.name)
        return v[len(v)-1]
    def get_size(self):
        return " MB {0:.2f}".format(self.userFile.size/1048576)

    userFile=models.FileField(upload_to='documents/')
    userFileUser=models.ForeignKey(SysUser,on_delete=models.CASCADE,blank=True,null=True)
    userFiledateAdded=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="userfile"


class Personnel(models.Model):
    manager=models.ForeignKey('SysUser',on_delete=models.SET_NULL,related_name='sarshift',null=True,blank=True)
    saloon=models.ForeignKey('Asset',on_delete=models.SET_NULL,related_name='saloon',null=True,blank=True)
    Pid = models.IntegerField()
    PNumber = models.BigIntegerField()
    CpCode = models.IntegerField()
    BranchCode = models.IntegerField()
    CardNo = models.IntegerField(blank=True, null=True)
    FName = models.CharField(max_length=40, blank=True, null=True)
    LName = models.CharField(max_length=50, blank=True, null=True)
    NCode = models.CharField(max_length=10, blank=True, null=True)
    BirthDate = models.CharField(max_length=10, blank=True, null=True)
    Father = models.CharField(max_length=30, blank=True, null=True)
    IdCardNo = models.BigIntegerField(blank=True, null=True)
    IssuedFrom = models.CharField(max_length=30, blank=True, null=True)
    BirthPlace = models.CharField(max_length=30, blank=True, null=True)
    Gender = models.CharField(max_length=1, blank=True, null=True)
    Nationality = models.SmallIntegerField(blank=True, null=True)
    Country = models.CharField(max_length=20, blank=True, null=True)
    Tel = models.CharField(max_length=12, blank=True, null=True)
    Mobile = models.CharField(max_length=11, blank=True, null=True)
    PostalCode = models.BigIntegerField(blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Kol = models.IntegerField(blank=True, null=True)
    Moin = models.IntegerField(blank=True, null=True)
    GTaf = models.IntegerField(blank=True, null=True)
    CTaf = models.IntegerField(blank=True, null=True)
    Markaz = models.IntegerField(blank=True, null=True)
    Dayere = models.IntegerField(blank=True, null=True)
    Picture = models.ImageField(blank=True, null=True)
    GruopCode = models.CharField(max_length=12, blank=True, null=True)
    OrganizCode = models.CharField(max_length=20, blank=True, null=True)
    TempEmploymentDate = models.CharField(max_length=10, blank=True, null=True)
    PermanentEmplymentDate = models.CharField(max_length=10, blank=True, null=True)
    Ekhrajdate = models.CharField(max_length=10, blank=True, null=True)
    ContractStartDate = models.CharField(max_length=10, blank=True, null=True)
    ContractFinishDate = models.CharField(max_length=10, blank=True, null=True)
    LeaveWorkDate = models.CharField(max_length=10, blank=True, null=True)
    RetiredDate = models.CharField(max_length=10, blank=True, null=True)
    DieDate = models.CharField(max_length=10, blank=True, null=True)
    InsuranceDate = models.CharField(max_length=10, blank=True, null=True)
    Consideration = models.CharField(max_length=250, blank=True, null=True)
    InsuranceNo = models.CharField(max_length=10, blank=True, null=True)
    InsuranceType = models.SmallIntegerField(blank=True, null=True)
    isActive = models.BooleanField(blank=True, null=True)
    FNameEn = models.CharField(max_length=40, blank=True, null=True)
    LNameEn = models.CharField(max_length=50, blank=True, null=True)
    Countryid = models.SmallIntegerField(blank=True, null=True)
    SanavatMonth = models.SmallIntegerField(blank=True, null=True)
    CpCodeSanad = models.IntegerField(blank=True, null=True)
    WebPass = models.CharField(max_length=100, blank=True, null=True)
    TelegramNumber = models.CharField(max_length=11, blank=True, null=True)
    Shift = models.CharField(max_length=2, blank=True, null=True)

    


    def __str__(self):
        return f"{self.FName} {self.LName}"
class PersonelFile(models.Model):
    def get_ext(self):
        v=os.path.splitext(self.woFile.name)
        return v[len(v)-1]
    def get_name(self):
        return os.path.basename(str(self.msgFile))
    def get_size(self):
        return " MB {0:.2f}".format(self.woFile.size/1048576)

    msgFile=models.FileField(upload_to='documents/Personel/%Y/%m/%d',max_length=200)
    msgFilePersonel=models.ForeignKey(Personnel, verbose_name="personel_file", on_delete=models.CASCADE,blank=True,null=True)
    msgFiledateAdded=models.DateTimeField(auto_now_add=True)
    msgFiledtype=models.IntegerField()
    msgFileName=models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        db_table="personelfile"
class HozurGhiab(models.Model):
    person=models.ForeignKey('Personnel',on_delete=models.CASCADE,related_name='person_hozur')
    registerd_by=models.ForeignKey('SysUser',on_delete=models.SET_NULL,related_name='manager',null=True,blank=True)
    incom_time = models.TimeField()
    outcome_time = models.TimeField()
    hdate = models.DateField(default=datetime.now().date())
    registerd_date = models.DateTimeField(auto_now_add=True)
    hozur = models.BooleanField(default=False)
    estehghaghi = models.BooleanField(default=False)
    estelaji = models.BooleanField(default=False)
    class Meta:
        db_table="hozurghiab"
        unique_together = ('person', 'hdate',)
