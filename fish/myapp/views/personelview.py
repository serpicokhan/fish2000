import csv
from datetime import datetime
from myapp.models import Personnel,PersonelFile,HozurGhiab,SysUser  # Replace 'myapp' with the name of your Django app
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

def doPaging(request,books):
    page=request.GET.get('page',1)
    paginator = Paginator(books, 5)
    wos=None
    try:
        wos=paginator.page(page)
    except PageNotAnInteger:
        wos = paginator.page(1)
    except EmptyPage:
        wos = paginator.page(paginator.num_pages)
    return wos
def list_personel(request):
    books=Personnel.objects.all()
    wos=doPaging(request,(books))


    return render(request, 'myapp/personel/personelList.html', {'fishes': wos,'title':'مشخصات','section':'list_personel'})


def view_profile(request,id):
    p=Personnel.objects.get(PNumber=id)
    pics=PersonelFile.objects.filter(msgFilePersonel=p).values('msgFile','msgFileName')
    form=PersonelForm(instance=p)
    return render(request, 'myapp/personel/profile.html', {'form':form,'title':'فیش حقوقی',\
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
                PNumber=int(row['PNumber']),
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
        if(users.count()>0):
            return render(request, 'myapp/personel/att2.html', {'user':manager,'personnel_list': users,'title':'مشخصات','section':'list_personel'})
        else:
            print(request.method)
            user_name=request.user
            manager=SysUser.objects.get(userId=request.user)
            wos=Personnel.objects.filter(manager=manager)
            return render(request, 'myapp/personel/att.html', {'user':user_name,'personnel_list': wos,'title':'مشخصات','section':'list_personel'})
    else:
        #return json response for ajax method
        data=dict()
        send_data = json.loads(request.body)
        date=DateJob.getTaskDate(send_data['hdate'])
        print(send_data,'date!!!!!!!!!!!!')

        manager=SysUser.objects.get(userId=request.user)
        users=HozurGhiab.objects.filter(hdate=date,person__in=Personnel.objects.filter(manager=manager))
        if(users.count()>0):
            data['result'] = render_to_string('myapp/personel/partialatt2.html', {
                'personnel_list': users
            })
            return JsonResponse(data)
        else:
            print(request.method)
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
        print("********")
        for i in data:
            print(i['name'])
            print(i['number'])
            print(DateJob.getTaskDate(i['hdate']))
            person=Personnel.objects.get(id=int(i['id']))
            hdate=DateJob.getTaskDate(i['hdate'])
            
            try:
                HozurGhiab.objects.create(person=person,\
                                        incom_time=i['inTimeValue'],outcome_time=i['outTimeValue'],\
                                        hdate=hdate,hozur=i['absentChecked'],\
                                        estehghaghi=i['estehghaghiChecked'],estelaji=i['estelajiChecked'],\
                                            registerd_by=registerd_user)
            except IntegrityError as e:
                o=HozurGhiab.objects.get(person=person,hdate=hdate)
                o.incom_time=i['inTimeValue']
                o.outcome_time=i['outTimeValue']
                o.hdate=hdate
                o.hozur=i['absentChecked']
                o.estehghaghi=i['estehghaghiChecked']
                o.estelaji=i['estelajiChecked']
                o.registerd_by=registerd_user
                o.save()
                
           
        dt['form_is_valid']=True

        return JsonResponse(dt)
    return HttpResponse('nothins saved')
def user_login(request):
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
       
        form = HozurForm(initial={'hdate':datetime.datetime.now()})
        # form=SysUserForm()
        return save_hozur_form(request, form, 'myapp/personel/partialHozurCreate.html',datetime.datetime.now())
@login_required
def save_hozur_form(request, form, template_name,reg_date):


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

    chips = Personnel.objects.exclude(manager__userId=request.user)
    context = {'form': form ,'chips': chips}


    data['html_hozur_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
##########################################################
def show_hozur_calendar(request):
    user=SysUser.objects.all()
    return render(request,'myapp/personel/admin_hozur_list.html',{'user':user})
def get_personel_calendar_info(request):
    data=[]
    user_info=HozurGhiab.objects.values_list('registerd_by','hdate').distinct()
    for i in user_info:
        data.append({'title': "برنامه نویسی",\
                'start': i[1],\
                'className': "bg-dark",\
                'id':i[0]})
    
    return JsonResponse(data,safe=False)
def get_hozur_list_detail(request):
    data=dict()
    manager=request.GET.get('id',False)
    hdate=request.GET.get('hdate',False)
    if(hdate and manager):
        user_list_raw=HozurGhiab.objects.filter(registerd_by=manager,hdate=hdate)
        user_list=[]
        
        data['html_hozur_data']=  render_to_string('myapp/personel/partialatt2.html', {
                'personnel_list': user_list_raw
            })
    return JsonResponse(data,safe=False)