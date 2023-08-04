import csv
from datetime import datetime
from myapp.models import Personnel  # Replace 'myapp' with the name of your Django app
from django.shortcuts import render
from django.core.paginator import *
from myapp.forms import PersonelForm
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
def list_personel(request):
    books=Personnel.objects.all()
    wos=doPaging(request,(books))


    return render(request, 'myapp/personel/personelList.html', {'fishes': wos,'title':'فیش حقوقی','section':'list_personel'})


def view_profile(request):
    form=PersonelForm()
    return render(request, 'myapp/personel/profile.html', {'form':form,'title':'فیش حقوقی','section':'view_profile'})

def convert_to_int(value):
    if(value == 'NULL' or value is None):
        return None
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
            print(row['InsuranceType'])
            personnel = Personnel(
                Pid=int(row['\ufeffPid']),
                PNumber=int(row['PNumber']),
                CpCode=int(row['CpCode']),
                BranchCode=int(row['BranchCode']),
                CardNo=int(row['CardNo']),
                FName=row['FName'],
                LName=row['LName'],
                NCode=row['NCode'],
                BirthDate=birth_date,
                Father=row['Father'],
                IdCardNo=int(row['IdCardNo']),
                IssuedFrom=row['IssuedFrom'],
                BirthPlace=row['BirthPlace'],
                Gender=row['Gender'],
                Nationality=int(row['Nationality']),
                Country=convert_to_int(row['Country']),
                Tel=row['Tel'],
                Mobile=row['Mobile'],
                PostalCode=int(row['PostalCode']),
                Address=row['Address'],
                Kol=int(row['Kol']),
                Moin=int(row['Moin']),
                GTaf=int(row['GTaf']),
                CTaf=int(row['CTaf']),
                Markaz=int(row['Markaz']),
                Dayere=int(row['Dayere']),
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
                Countryid=int(row['Countryid']),
                SanavatMonth=int(row['SanavatMonth']),
                CpCodeSanad=int(row['CpCodeSanad']),
                WebPass=row['WebPass'],
                TelegramNumber=row['TelegramNumber'],
            )
            personnel.save()