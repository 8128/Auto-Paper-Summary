from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import *


def index(request):
    return render(request, 'summary_index/index.html')


# def short_summary(request):
#     return render(request, 'summary_index/short_summary.html')
#
#
# def long_summary(request):
#     return render(request, 'summary_index/long_summary.html')


def user_info(request):
    ip_addr = request.META['REMOTE_ADDR']

    user_obj = UserInfo.objects.filter(ip=ip_addr)
    if not user_obj:
        UserInfo.objects.create(ip=ip_addr)
    #     res = UserInfo.objects.create(ip=ip_addr)
    #     ip_add_id = res.id
    # else:
    #     ip_add_id = user_obj[0].id
    #
    # ShortTextDB.objects.create(short_text="",user_ip = ip_add_id)

    result = {
        "status": "success",
        "info": "User Info",
        "IP": ip_addr,
    }

    return HttpResponse(json.dumps(result), content_type="application/json")


def history(request):
    ip_list = UserInfo.objects.all()
    info = []
    for item in ip_list:
        info.append(item.ip)

    result = {
        "status": "success",
        "INFO": info
    }

    return HttpResponse(json.dumps(result), content_type="application/json")
