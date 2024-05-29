'''
 fmt = getattr(settings, 'LOG_FORMAT', None)
 lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

 logging.basicConfig(format=fmt, level=lvl)
 logging.debug(nemailbject.OrderId.id)
 '''
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Sum
import jdatetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators import csrf
import django.core.serializers
import logging
from django.conf import settings

from myapp.models.fish import *
from myapp.models.message import *
#from django.core import serializers
import json
from django.forms.models import model_to_dict
from myapp.forms import MessageForm
from django.urls import reverse_lazy,reverse
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.core.paginator import *
from openpyxl import load_workbook
from django.db.models import Q
import os
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
def doPaging(request,books):
    page=request.GET.get('page',1)
    paginator = Paginator(books, 8)
    wos=None
    try:
        wos=paginator.page(page)
    except PageNotAnInteger:
        wos = paginator.page(1)
    except EmptyPage:
        wos = paginator.page(paginator.num_pages)
    return wos

@login_required
@permission_required('myapp.view_fish')
def list_fish(request):
    #
    books=Fish.objects.all()
    wos=doPaging(request,(books))


    return render(request, 'myapp/fish/fishList.html', {'fishes': wos,'title':'فیش حقوقی','section':'list_mail'})
def search_fish(request):
    q=request.GET.get("q",False)
    data=dict()
    if(q):
    #
        books=Fish.objects.filter(Q(name__contains=q)|Q(code=q)|Q(code_meli=q))
        wos=doPaging(request,(books))
        data['result']= render_to_string('myapp/fish/partialFishList.html', {
                'fishes': wos
            })
        return JsonResponse(data)

    books=Fish.objects.all()
    wos=doPaging(request,(books))
    data['result']= render_to_string('myapp/fish/partialFishList.html', {
            'fishes': wos
        })
    return JsonResponse(data)
def details_fish(request):
    #
    # books = Message.objects.filter().order_by('-id')
    # wos=doPaging(request,(books))
    code_meli=request.POST.get('code_meli',False)
    code=request.POST.get('code',False)
    mah1=request.POST.get('mah1',1)
    sal=request.POST.get('year',1403)

    print("mah1",mah1)
    month=['','فروردین','ارديبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']

    wos=Fish.objects.filter(code=code,code_meli=code_meli,mah=mah1,sal=sal)
    if(wos.count()>0):
        karkard=int(wos[0].monthly_hoghugh)/int(wos[0].daily_hoghugh)

        return render(request, 'myapp/fish/fishDetal.html', {'c': wos[0],'karkard':karkard,'title':'صندوق دریافت','section':'list_mail','mah':month[int(wos[0].mah)],'sal':wos[0].sal})
    return render(request, 'myapp/page-error-404.html', {'ss':''})
@login_required
@transaction.atomic
def fish_upload(request):
    def iter_rows(ws):
        for row in ws.iter_rows():
            yield [cell.value for cell in row]
    if request.method == 'POST':
        # print("here!!!",request.FILES)
        my_file=request.FILES.get('file')
        # print(my_file.name)
        month=request.POST.get('month_select',False)
        sal=request.POST.get('sal_select',False)




        msg=MessageFile.objects.create(msgFile=my_file)
        workbook = load_workbook(filename='media/'+msg.msgFile.name)
        ws = workbook.active
        # print(list(iter_rows(ws))[1])
        # Fish.objects.all().delete()
        item_new=Fish(pk=None)
        item_old=Fish(pk=None)

        for i in list(iter_rows(ws)):
            if(i[20]==None):
                pass
            elif(not str(i[30]).isdigit()):
                pass
            else:
                if(i[30] != None):
                    item_new.pk=None
                    item_new.mah=month
                    item_new.sal=sal


                    item_new.mande_morakhasi="{0}:{1}:{2}".format(i[32],i[33],i[34])
                    item_new.code=i[30] if(i[30]) else 0
                    item_new.code_meli=i[29] if(i[29]) else 0
                    item_new.name=i[28] if(i[28]) else 0
                    item_new.daily_hoghugh=i[27] if(i[27]) else 0
                    item_new.karkard=i[26] if(i[26]) else 0
                    item_new.monthly_hoghugh=i[25] if(i[25]) else 0
                    item_new.bon=i[24] if(i[24]) else 0
                    item_new.maskan=i[23] if(i[23]) else 0
                    item_new.nobate_kari=i[22] if(i[22]) else 0
                    item_new.paye_sanavat=i[21] if(i[21]) else 0
                    item_new.ovlad_moavaghe=i[20] if(i[20]) else 0
                    item_new.ovlad=i[19] if(i[19]) else 0
                    item_new.ezafe_kar=i[18] if(i[18]) else 0
                    item_new.padash=i[17] if(i[17]) else 0
                    item_new.eslahe_hoghugh=i[16] if(i[16]) else 0
                    item_new.randeman=i[15] if(i[15]) else 0
                    item_new.jome_kari=i[14] if(i[14]) else 0
                    item_new.ravande_mahe_ghabl=i[13] if(i[13]) else 0
                    item_new.maliat=i[12] if(i[12]) else 0
                    item_new.haghe_bime=i[11] if(i[11]) else 0
                    item_new.mosaede=i[10] if(i[10]) else 0
                    item_new.kasre_hoghugh=i[9] if(i[9]) else 0
                    item_new.vame_dakheli=i[8] if(i[8]) else 0
                    item_new.bime_takmili=i[7] if(i[7]) else 0
                    item_new.vame_aghsati=i[6] if(i[6]) else 0
                    item_new.bime_azad=i[5] if(i[5]) else 0
                    item_new.jarime=i[4] if(i[4]) else 0
                    item_new.pool_khurd=i[3] if(i[3]) else 0
                    item_new.morakhasi=i[2] if(i[2]) else 0
                    item_new.ezafe_kar_time=i[1] if(i[1]) else 0
                    item_new.estelaji=i[0] if(i[0]) else 0
                    item_new.haghe_tahol=i[36] if(i[36]) else 0
                    item_new.tatil_kar=i[35] if(i[35]) else 0
                    item_new.save()




        data=dict()
        data["id"]=msg.id
        return JsonResponse(data)
        # return HttpResponse('')
    return JsonResponse({'post':'fasle'})
@permission_required('myapp.view_fish')
def fish_create(request):
    if (request.method == 'POST'):

        return HttpResponseRedirect(reverse('list_mail'))
    else:

        # form = MessageForm({'fromUser':SysUser.objects.get(userId=request.user.id),'messageStatus':2})
        # form.isupdated=False
        # return save_mail_form(request, form, 'myapp/mail/partialMailCreate.html')
        return render(request, 'myapp/fish/partialFishCreate.html', {'form':''})
def fish_view(request,id):
    pass
def register_shekayat(reuqest,id):
    fish=Fish.objects.get(id=id)
    shekayat=request.POST.get('shekayat',False)
    if(shekayat):
        fish.shekayat=shekayat
        fish.save()

        return HttpResponseRedirect(reverse('index'))
