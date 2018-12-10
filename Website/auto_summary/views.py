from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from .models import *
from .forms import *


def index(request):
    return render(request, 'summary_index/index.html')


def summary(request):
    return render(request, 'summary_index/summary.html')


def about(request):
    return render(request, 'summary_index/about.html')


def short_input(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/summary_index/summary')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


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
