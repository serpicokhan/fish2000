from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from myapp.business.UserUtility import *
from django.contrib.auth.decorators import login_required
from myapp.models import SysUser
# @login_required
def index(request):
    month=['فروردین','ارديبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
    # UserUtility.get_user_list(request)
    # return render(request,"myapp/index.html",{"today" : today})
    return render(request,"myapp/entrance/login.html",{"today" : month})
