from django.db import models
from myapp.models.users import *
class Fish(models.Model):

    # khalese_pardakhti = models.CharField("خالص پرداختی",max_length=255,blank=True,null=True)
    # jame_kosurat = models.CharField("جمع کسورات",max_length=255,blank=True,null=True)
    # sayere_kosurat = models.CharField("سایر کسورات",max_length=255,blank=True,null=True)
    # vam = models.CharField("وام",max_length=255,blank=True,null=True)
    #
    #
    #
    # nakhalese_pardakhti = models.CharField("ناخالص پرداختی",max_length=255,blank=True,null=True)
    # sayere_mazaya = models.CharField("سایر مزایا",max_length=255,blank=True,null=True)




    def get_bime(self):
        return "{:,.0f}".format((float(self.monthly_hoghugh)+float(self.bon)+float(self.maskan))*0.07)
    def get_karkard(self):
        if(float(self.daily_hoghugh)==0):
            return 0
        return float(self.monthly_hoghugh)/float(self.daily_hoghugh)
    def get_gheibat(self):
        if(int(self.mah)<=6):
            return 31-self.get_karkard()-float(self.estelaji)
        elif(int(self.mah)==12):
            return 29-self.get_karkard()-float(self.estelaji)
        else:
            return 30-self.get_karkard()-float(self.estelaji)

    def get_bime_simple(self):
        # return (float(self.monthly_hoghugh)+float(self.bon)+float(self.maskan))*0.07
        return float(self.haghe_bime)
    def get_majmu_kosurat(self):
        return "{:,.0f}".format(self.get_majmu_kosurat_simple())
    def get_pardakhtha(self):
        return "{:,.0f}".format(self.get_pardakhtha_simple())
    def get_majmu_kosurat_simple(self):
        return self.get_bime_simple()+(float(self.maliat)+float(self.pool_khurd)+float(self.vame_dakheli)+float(self.vame_aghsati)+float(self.bime_azad)+float(self.bime_takmili)+float(self.kasre_hoghugh)+float(self.jarime)+float(self.mosaede))
    def get_pardakhtha_simple(self):
        return (float(self.monthly_hoghugh)+float(self.ovlad)+float(self.ovlad_moavaghe)+float(self.randeman)+float(self.maskan)+float(self.bon)+float(self.ezafe_kar)+float(self.paye_sanavat)+float(self.jome_kari)+float(self.ravande_mahe_ghabl)+float(self.nobate_kari)+float(self.eslahe_hoghugh)+float(self.padash))
    def get_daryafti(self):
        return "{:,.0f}".format(self.get_pardakhtha_simple()-self.get_majmu_kosurat_simple())


    sal = models.CharField("خالص پرداختی",max_length=255,blank=True,null=True)
    mah = models.CharField("خالص پرداختی",max_length=255,blank=True,null=True)
    shekayat= models.CharField("مانده مرخصی",max_length=255,blank=True,null=True)
    mande_morakhasi= models.CharField("مانده مرخصی",max_length=255,blank=True,null=True)
    estelaji= models.CharField("استعلاجی",max_length=255,blank=True,null=True)
    ezafe_kar_time= models.CharField("اضافه کار",max_length=255,blank=True,null=True)
    morakhasi= models.CharField("مرخصی",max_length=255,blank=True,null=True)
    pool_khurd= models.CharField("پول خورد",max_length=255,blank=True,null=True)
    jarime= models.CharField("جریمه",max_length=255,blank=True,null=True)
    bime_azad= models.CharField("بیمه آزاد",max_length=255,blank=True,null=True)
    vame_aghsati= models.CharField("وام اقساطی",max_length=255,blank=True,null=True)
    bime_takmili= models.CharField("بیمه تکمیلی",max_length=255,blank=True,null=True)
    vame_dakheli= models.CharField("وام داخلی",max_length=255,blank=True,null=True)
    kasre_hoghugh= models.CharField("کسر حقوق",max_length=255,blank=True,null=True)
    mosaede = models.CharField("مساعده",max_length=255,blank=True,null=True)
    haghe_bime = models.CharField("حق بیمه",max_length=255,blank=True,null=True)
    maliat = models.CharField("مالیات",max_length=255,blank=True,null=True)
    ravande_mahe_ghabl = models.CharField("روند ماه قبل",max_length=255,blank=True,null=True)
    jome_kari = models.CharField("جمعه کاری",max_length=255,blank=True,null=True)
    randeman = models.CharField("راندمان",max_length=255,blank=True,null=True)
    eslahe_hoghugh = models.CharField("اصلاح حقوق",max_length=255,blank=True,null=True)
    padash = models.CharField("پاداش",max_length=255,blank=True,null=True)


    ezafe_kar = models.CharField("اضافه کار",max_length=255,blank=True,null=True)
    nemidunam = models.CharField("??",max_length=255,blank=True,null=True)
    ovlad = models.CharField("اولاد",max_length=255,blank=True,null=True)
    ovlad_moavaghe = models.CharField("اولاد معوقه",max_length=255,blank=True,null=True)
    paye_sanavat = models.CharField("پایه سنوات",max_length=255,blank=True,null=True)
    nobate_kari = models.CharField("نوبت کاری",max_length=255,blank=True,null=True)
    maskan= models.CharField("مسکن",max_length=255,blank=True,null=True)
    bon = models.CharField("بن",max_length=255,blank=True,null=True)

    monthly_hoghugh = models.CharField("حقوق ماهانه",max_length=255,blank=True,null=True)
    karkard = models.CharField("کارکرد به روز",max_length=255,blank=True,null=True)

    daily_hoghugh = models.CharField("حقوق روزانه",max_length=255,blank=True,null=True)
    name = models.CharField("نام",max_length=255,blank=True,null=True)
    code_meli = models.CharField("کد ملی",max_length=255,blank=True,null=True)
    code = models.CharField("کد پرسنلی",max_length=255,blank=True,null=True)







    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="fish"
        ordering = ('date_added',)
