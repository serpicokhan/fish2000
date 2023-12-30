
import csv
from datetime import datetime

from myapp.models import Personnel,PersonelFile,HozurGhiab,SysUser,Asset,AssetUser  # Replace 'myapp' with the name of your Django app
from django.shortcuts import render
from django.core.paginator import *
from django.http import JsonResponse
from myapp.forms import PersonelForm,HozurForm
from django.views.decorators import csrf
from django.db.models import Q
import os
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from myapp.forms import LoginForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
import json
from myapp.business.DateJob import *
from django.db import IntegrityError
from django.contrib.auth.models import User,Group
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from jdatetime import datetime as dt
def doPaging(request,books):
    page=request.GET.get('page',1)
    paginator = Paginator(books, 60)
    wos=None
    try:
        wos=paginator.page(page)
    except PageNotAnInteger:
        wos = paginator.page(1)
    except EmptyPage:
        wos = paginator.page(paginator.num_pages)
    return wos
@permission_required('myapp.view_personnnel')
def list_personel(request):
    asset_param=request.GET.get('asset_param',False)
    manager_param=request.GET.get('manager_param',False)

    books=Personnel.objects.all()
    if(asset_param and asset_param!='-1'):
        books=books.filter(saloon=asset_param)
    if(manager_param  and asset_param!='-1'):
        books=books.filter(manager=manager_param)
    wos=doPaging(request,list(books))
    group = Group.objects.get(name='manager')
    asset=Asset.objects.all()


# Get all users belonging to the group
    users_in_group = group.user_set.all()
    users=SysUser.objects.filter(userId__in=users_in_group).order_by('fullName')
    return render(request, 'myapp/personel/personelList.html', {'fishes': wos,'title':'مشخصات','section':'list_personel','manager':users,'asset':asset,'asset_param':asset_param,'manager_param':manager_param})

@permission_required('myapp.view_personnnel')
def view_profile(request,id):
    p=Personnel.objects.get(id=id)
    pics=PersonelFile.objects.filter(msgFilePersonel=p).values('msgFile','msgFileName')
    form=PersonelForm(instance=p)
    return render(request, 'myapp/personel/profile.html', {'form':form,'title':'پروفایل',\
                                                           'section':'view_profile','pics':list(pics)})

def convert_to_int(value):
    if(value == 'NULL' or value is None):
        return 0
    else:
        return int(value)


     # if value is not None  else None
def convert_to_bool(value):
    if value is None:
        return None
    try:
        return bool(int(value))
    except (ValueError, TypeError):
        return None
def insert_personel_data_from_csv(request):
    csv_file='personel.csv'
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:

            # Convert date strings to datetime objects
            birth_date = row['BirthDate']
            # temp_emp_date = datetime.strptime(row['TempEmploymentDate'], '%Y/%m/%d').date()
            # perm_emp_date = datetime.strptime(row['PermanentEmplymentDate'], '%Y/%m/%d').date()
            # ekhraj_date = datetime.strptime(row['Ekhrajdate'], '%Y/%m/%d').date()
            contract_start_date = row['ContractStartDate']
            contract_finish_date =row['ContractFinishDate']
            # leave_work_date = datetime.strptime(row['LeaveWorkDate'], '%Y/%m/%d').date()
            # retired_date = datetime.strptime(row['RetiredDate'], '%Y/%m/%d').date()
            # die_date = datetime.strptime(row['DieDate'], '%Y/%m/%d').date()
            # insurance_date = datetime.strptime(row['InsuranceDate'], '%Y/%m/%d').date()

            # Create a Personnel object and save it to the database
            print(row['\ufeffPid'])
            personnel = Personnel(
                Pid=row['\ufeffPid'],
                PNumber=(row['PNumber']),
                CpCode=int(row['CpCode']),
                BranchCode=int(row['BranchCode']),
                CardNo=(row['CardNo']),
                FName=row['FName'],
                LName=row['LName'],
                NCode=row['NCode'],
                BirthDate=birth_date,
                Father=row['Father'],
                IdCardNo=(row['IdCardNo']),
                IssuedFrom=row['IssuedFrom'],
                BirthPlace=row['BirthPlace'],
                Gender=row['Gender'],
                Nationality=(row['Nationality']),
                Country=row['Country'],
                Tel=row['Tel'],
                Mobile=row['Mobile'],
                PostalCode=(row['PostalCode']),
                Address=row['Address'],
                Kol=(row['Kol']),
                Moin=(row['Moin']),
                GTaf=(row['GTaf']),
                CTaf=(row['CTaf']),
                Markaz=(row['Markaz']),
                Dayere=(row['Dayere']),
                GruopCode=row['GruopCode'],
                OrganizCode=row['OrganizCode'],
                # TempEmploymentDate=temp_emp_date,
                # PermanentEmplymentDate=perm_emp_date,
                # Ekhrajdate=ekhraj_date,
                ContractStartDate=contract_start_date,
                ContractFinishDate=contract_finish_date,
                # LeaveWorkDate=leave_work_date,
                # RetiredDate=retired_date,
                # DieDate=die_date,
                # InsuranceDate=insurance_date,
                Consideration=row['Consideration'],
                InsuranceNo=row['InsuranceNo'],
                InsuranceType=convert_to_int(row['InsuranceType']),
                isActive=convert_to_bool(row['isActive']),
                FNameEn=row['FNameEn'],
                LNameEn=row['LNameEn'],
                # Countryid=int(row['Countryid']),
                # SanavatMonth=int(row['SanavatMonth']),
                # CpCodeSanad=int(row['CpCodeSanad']),
                WebPass=row['WebPass'],
                TelegramNumber=row['TelegramNumber'],
            )
            personnel.save()
    return HttpResponse('saved succesfully')
def login_to_load_file(request):
    return render(request,'myapp/personel/login.html',{})
def file_upload_doc(request):
        cp=request.POST.get('code',False)
        code_meli=request.POST.get('code_meli',False)
        p=Personnel.objects.get(NCode='{}'.format(code_meli))
        p_files_type=PersonelFile.objects.filter(msgFilePersonel=p).values('msgFiledtype')
        p_files=PersonelFile.objects.filter(msgFilePersonel=p).values('msgFile','id','msgFileName')
        return render(request, 'myapp/files.html', {'cp':cp,'code_meli':code_meli,\
                                                    'file_types':list(p_files_type),'files':list(p_files)})
def update_personel(request,id):
    company= get_object_or_404(Personnel, id=id)
    template=""
    if (request.method == 'POST'):
        form = PersonelForm(request.POST, instance=company)
        if(form.is_valid):
            form.save()
            return list_personel(request)

@csrf_exempt
def handle_file_upload(request):

    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        code=request.GET.get("code",False)
        code_meli=request.GET.get("code_meli",False)
        btn_name=request.GET.get("btnName",False)
        btn_type=request.GET.get("btnType",False)
        p=Personnel.objects.get(NCode='{}'.format(code_meli))

        # New directory where the files will be saved (named with the current date and time)
        # upload_directory = f'media/uploads/{current_datetime}/'
        # os.makedirs(upload_directory, exist_ok=True)
        # # Replace 'uploads/' with the desired directory path to save the uploaded files
        # with open(os.path.join(upload_directory, uploaded_file.name), 'wb+') as destination_file:
        #     for chunk in uploaded_file.chunks():
        #         destination_file.write(chunk)
        p_file=PersonelFile.objects.create(msgFile=uploaded_file,msgFiledtype=btn_type,msgFilePersonel=p,msgFileName=btn_name)

        return JsonResponse({'message': 'File uploaded successfully.', 'file_name': uploaded_file.name,'id':p_file.id})
    else:
        return JsonResponse({'error': 'No file was uploaded.'})

def remove_person_file(request,id):
    file=PersonelFile.objects.get(id=id)
    file.delete()
    data=dict()
    data['file_is_valied']=True
    return JsonResponse(data)
@csrf_exempt
@login_required(login_url="/userlogin/")
def view_att(request):
    if(request.method=='GET'):
        manager=SysUser.objects.get(userId=request.user)
        users=HozurGhiab.objects.filter(hdate=datetime.datetime.now().date(),registerd_by=manager)
        # if(users.count()>0):
        #     return render(request, 'myapp/personel/try_tommarow.html', {'user':manager,'personnel_list': users,'title':'مشخصات','section':'list_personel'})
        # else:
        date_obj = datetime.datetime.now()
        jalali_date=jdatetime.date.fromgregorian(date=date_obj)
        formatted_date = f"{jalali_date.year:04d}-{jalali_date.month:02d}-{jalali_date.day:02d}"
        user_name=request.user
        manager=SysUser.objects.get(userId=request.user)
        wos=Personnel.objects.filter(manager=manager).order_by('title')
        return render(request, 'myapp/personel/att.html', {'user':user_name,'personnel_list': wos,'title':'مشخصات','section':'list_personel','dt':formatted_date})
    else:
        #return json response for ajax method
        data=dict()
        send_data = json.loads(request.body)
        date=DateJob.getTaskDate(send_data['hdate'])

        manager=SysUser.objects.get(userId=request.user)
        users=HozurGhiab.objects.filter(hdate=date,person__in=Personnel.objects.filter(manager=manager))
        if(users.count()>0):
            data['result'] = render_to_string('myapp/personel/partialatt2.html', {
                'personnel_list': users
            })
            return JsonResponse(data)
        else:
            user_name=request.user
            manager=SysUser.objects.get(userId=request.user)
            wos=Personnel.objects.filter(manager=manager)
            data['result'] = render_to_string('myapp/personel/partialatt2.html', {
                'personnel_list': users
            })

        return JsonResponse(data)
@login_required(login_url="/userlogin/")
@csrf_exempt
def save_personel_att(request):
    if(request.method=='POST'):
        dt={}
        data = json.loads(request.body)
        registerd_user=SysUser.objects.get(userId=request.user)
        for i in data:
            person=Personnel.objects.get(id=int(i['id']))
            hdate=DateJob.getTaskDate(i['hdate'])
            ezafekar=True if i['ezafe_kar'] == 'true' else False
            try:
                HozurGhiab.objects.create(person=person,\
                                        incom_time=i['inTimeValue'],outcome_time=i['outTimeValue'],\
                                        hdate=hdate,hozur=i['absentChecked'],\
                                        estehghaghi=i['estehghaghiChecked'],estelaji=i['estelajiChecked'],\
                                        registerd_by=registerd_user,title=i['title2'],is_ezafekar=ezafekar)
            except IntegrityError as e:
                o=HozurGhiab.objects.get(person=person,hdate=hdate)
                o.incom_time=i['inTimeValue']
                o.outcome_time=i['outTimeValue']
                o.hdate=hdate
                o.hozur=i['absentChecked']
                o.estehghaghi=i['estehghaghiChecked']
                o.estelaji=i['estelajiChecked']
                o.title=int(i['title2'])
                o.registerd_by=registerd_user
                o.is_ezafekar=ezafekar
                o.save()


        dt['form_is_valid']=True

        return JsonResponse(dt)
    return HttpResponse('nothins saved')
def user_login2(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        user = authenticate(request,
        username=cd['username'],
        password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('view_att')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'myapp/personel/managerlogin.html', {'form': form})
@login_required
def hozur_create(request):
    if (request.method == 'POST'):
        form = HozurForm(request.POST, files=request.FILES)
        return save_hozur_form(request, form, 'myapp/personel/partialHozurCreate.html')
    else:
        excluded_persons=request.GET.get('ids',None)
        form = HozurForm(initial={'hdate':datetime.datetime.now()})
        ex_p=None
        # form=SysUserForm()
        if(excluded_persons):
            ex_p=excluded_persons.split(',')
        return save_hozur_form(request, form, 'myapp/personel/partialHozurCreate.html',datetime.datetime.now(),exclueded_persons=ex_p)
@login_required
def save_hozur_form(request, form, template_name,reg_date,exclueded_persons=None):


    data = dict()
    if (request.method == 'POST'):
        if form.is_valid():


            form.save(commit=False)
            form.instance.registerd_by=request.user.person_hozur
            data['form_is_valid'] = True
            books = HozurGhiab.objects.filter(hdate=reg_date,registerd_by=request.user.person_hozur)

            data['html_hozur_list'] = render_to_string('myapp/personel/partialatt2.html', {
                'personnel_list': books
            })
        else:
            data['form_is_valid'] = False
            print(form.errors)


    saloon_id=Personnel.objects.filter(manager__userId=request.user).first().saloon
    chips = Personnel.objects.exclude(manager__userId=request.user).filter(saloon=saloon_id)
    if(exclueded_persons):
        chips=chips.exclude(id__in=exclueded_persons)
    context = {'form': form ,'chips': chips}


    data['html_hozur_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
##########################################################
@permission_required('myapp.view_personnnel')
def show_hozur_calendar(request):
    user=SysUser.objects.all()
    return render(request,'myapp/personel/admin_hozur_list.html',{'user':user})
def get_personel_calendar_info(request):
    data=[]
    manager=request.GET.get('manager',False)
    print(manager,'manager')
    user_info=HozurGhiab.objects.filter(registerd_by=manager).values_list('registerd_by','hdate').distinct()
    for i in user_info:
        data.append({'title': " حضور غیاب",\
                'start': '{} 10:00:00'.format(i[1]),\
                'className': "bg-primary",\
                'id':i[0]})

    return JsonResponse(data,safe=False)
@permission_required('myapp.view_personnnel')
def get_hozur_list_detail(request):
    data=dict()
    manager=request.GET.get('id',False)
    manager_name=SysUser.objects.get(id=manager).fullName
    hdate=request.GET.get('hdate',False)
    if(hdate and manager):
        user_list_raw=HozurGhiab.objects.filter(registerd_by=manager,hdate=hdate).order_by('person__LName')
        user_list=[]
        date_obj = datetime.datetime.strptime(hdate, "%Y-%m-%d")
        jalali_date=jdatetime.date.fromgregorian(date=date_obj)
        formatted_date = f"{jalali_date.year:04d}/{jalali_date.month:02d}/{jalali_date.day:02d}"


    return render(request,'myapp/personel/hozurdetaillist.html',{'personnel_list': user_list_raw,'date':formatted_date,'manager_name':manager_name,'hdate':hdate,'manager':manager})



def save_Personel_form(request,form,template):
    pass
@permission_required('myapp.view_personnnel')
def personel_create(request):
    if (request.method == 'POST'):
        form = PersonelForm(request.POST)
        if(form.is_valid()):
            form.save()
            return list_personel(request)
    else:

        form = PersonelForm()
        return render(request,'myapp/personel/new_profile.html',{'form':form})
        # return save_Personel_form(request, form, 'cmms/maintenancetype/partialMaintenanceTypeCreate.html')

def get_manager_by_makan(request):
    asset=request.GET.get("q",False)
    if(asset):
        data=dict()
        ps=Personnel.objects.filter(saloon__id=asset).distinct()
        data['result'] = render_to_string('myapp/personel/partialmanagername.html', {
                'personnel_list': ps
            })
        return JsonResponse(data)
@csrf_exempt
def delete_personel(request,id):
        if(request.method=="POST"):
            p1=Personnel.objects.get(id=id)
            p1.delete()
            data=dict()
            data["valid"]=True
            return JsonResponse(data)
def search_personel(request):
    q=request.GET.get("q",False)
    asset_param=request.GET.get("asset_param",False)

    manager_param=request.GET.get("manager_param",False)

    # books=Personnel.objects.all()
    # wos=doPaging(request,(books))
    names = q.split()

    group = Group.objects.get(name='manager')
    asset=Asset.objects.all()
    users_in_group = group.user_set.all()
    users=SysUser.objects.filter(userId__in=users_in_group).order_by('fullName')
    data=dict()
    # if(q and len(names)==1):
    # #
    #     books=Personnel.objects.filter(Q(FName__contains=q)|Q(LName__contains=q)|Q(PNumber=q)|Q(NCode=q))
    #     wos=doPaging(request,list(books))

    # elif(q and len(names)>1):
    #     # first_name, last_name = names
    #     books=Personnel.objects.filter(Q(FName__contains=names[0]) & Q(LName__contains=names[1]))
    #     wos=doPaging(request,list(books))

    #     # print(Personnel.objects.filter(Q(FName__contains=first_name) & Q(LName__contains=last_name)).query)
    search_words = q.split()

# Initialize an empty Q object to build the query dynamically
    query = Q()

    # Loop through each word in the search term and add it to the query
    for word in search_words:
        # Add conditions for both fname and lname
        query |= Q(FName__icontains=word) | Q(LName__icontains=word)
        # query |= Q(FName__exact=word) | Q(LName__exact=word)
    # for word in search_words:
    #     if ' ' in word:
    #         query |= Q(FName__exact=word) | Q(LName__exact=word)


# Perform the query on your model
    if(len(search_words)>0):
        results = Personnel.objects.filter(query)
        wos=doPaging(request,list(results))

    else:
        books=Personnel.objects.all()
        wos=doPaging(request,list(books))
    if(asset_param!='-1'):
        books=books.filter(saloon=asset_param)
        wos=doPaging(request,list(books))

    if(manager_param!='-1'):
        books=books.filter(manager=manager_param)
        wos=doPaging(request,list(books))






    return render(request,'myapp/personel/personelList.html',{'fishes':wos,'title':'مشخصات','section':'list_personel','manager':users,'asset':asset,'q':q,'manager_param':manager_param,'asset_param':asset_param})
def getTitle(request):
    choices=[
            (0, 'سرشیفت',[1,2,3,4]),
            (1, 'مقدمات',[1,2,3]),
            (2, 'پاساژ',[1,2,3]),
            (3, 'فبنیشر',[1,2,3]),
            (26, 'ریبریکر',[1,2,3]),
            (4, 'سردافر',[1,2,3]),
            (5, 'رینگ',[1,2,3]),
            (6, 'لاکنی',[1,2,3]),
            (8, 'اتوکنر',[1,2,3]),
            (7, 'دولاتاب',[1,2,3]),
            (9, 'خدمات',[1,2,3]),
            (10, 'ssm',[1,2,3]),
            (11, 'هیت ست',[1,2,3]),
            (12, 'تاپس',[1,2,3]),
            (13, 'سرپرست',[4]),
            (14, 'آزمایشگاه',[4]),
            (15, 'رنگکشی',[4]),
            (16, 'آبگیر',[4]),
            (17, 'کوب',[4]),
            (18, 'رزرو دیگ',[4]),
            (19, 'استلام',[4]),
            (20, 'کوب کوچک',[4]),
            (21, 'لیفتراک',[4]),
            (22, 'پرس ضایعات',[4]),
            (23, 'پرس و خشک کن',[4]),
            (24, 'لیفتراک ریسندگی',[4]),
            (25, 'کاردینگ',[1,2,3]),
            ]

    id_user=request.GET.get("id",False)
    if(id_user):
        x=Personnel.objects.get(id=id_user).saloon.id
        choices = [(id, title, diff_id) for id, title, diff_id in choices if x in diff_id]





    data=dict()
    # sorted_choices = sorted(choices, key=lambda x: x[1])
    sorted_choices = choices

    data['html_hozur_form']=render_to_string('myapp/personel/partialTitle.html',{'chips':sorted_choices})
    return JsonResponse(data)

def show_hozur_success(request):
    return render(request,'myapp/personel/save_msg.html')
@csrf_exempt
def hozur_delete(request):
    data=dict()
    manager=request.GET.get('manager',False)
    hdate=request.GET.get('hdate',False)
    if(hdate and manager):
        plist=HozurGhiab.objects.filter(registerd_by__id=manager,hdate=hdate)
        for i in plist:
            i.delete()
        data['form_is_valid']=True
    return JsonResponse(data)
def get_personel_breig_info(request):
    makan=request.GET.get("makan",False)
    data=dict()
    result=[]
    if(makan):
        managers_in_saloon_1 = AssetUser.objects.filter(AssetUserAssetId__id=makan).values("AssetUserUserId")
        managers = SysUser.objects.filter(id__in=managers_in_saloon_1)

        date_obj = datetime.datetime.now()
        jalali_date=jdatetime.date.fromgregorian(date=date_obj)
        formatted_date = f"{jalali_date.year:04d}-{jalali_date.month:02d}-{jalali_date.day:02d}"

        for i in managers:
            users=HozurGhiab.objects.filter(hdate='2023-12-29',registerd_by=i)
            result.append({'shiftId':i.id,'shiftName':i.fullName,'personel_count':users.count(),'abset_count':users.filter(hozur=False).count(),'ezafe_kar':users.filter(is_ezafekar=True).count()})
        data['result'] = render_to_string('myapp/personel/partialManagerList.html', {
                'personnel_list': result
            })
        data['header'] = render_to_string('myapp/personel/manager_list_header.html', {
                'personnel_list': result
            })

    return JsonResponse(data)


@permission_required('myapp.view_personnnel')
def list_personel_breif(request):

    asset=Asset.objects.all()


# Get all users belonging to the group


    # Retrieve the manager objects
    
    return render(request, 'myapp/personel/managerList.html', {'title':'مشخصات','section':'list_personel','asset':asset})
