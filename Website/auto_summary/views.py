from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from .models import *
from .forms import *
from .text_summary import *


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            input_user = form.cleaned_data['user_name']
            input_email = form.cleaned_data['user_email']
            input_message = form.cleaned_data['user_message']
            UserFeedBack.objects.create(user_name=input_user, user_email=input_email, user_message=input_message)
            return render(request, 'summary_index/thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'summary_index/index.html', {'emailform': form})


def summary(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ShortTextForm(request.POST)
        form_feedback = ContactForm(request.POST)
        # check whether it's valid:
        if form_feedback.is_valid():
            input_user = form_feedback.cleaned_data['user_name']
            input_email = form_feedback.cleaned_data['user_email']
            input_message = form_feedback.cleaned_data['user_message']
            UserFeedBack.objects.create(user_name=input_user, user_email=input_email, user_message=input_message)
            return render(request, 'summary_index/thankyou.html')
        elif form.is_valid():
            input_data = form.cleaned_data['short_input']
            output_summary = short_text_summary(input_data)
            if hasattr(output_summary, 'errormessage'):
                return render(request, 'summary_index/summary.html', {'form': form, 'error': str(output_summary.errormessage), 'emailform': form_feedback})
            else:
                return render(request, 'summary_index/summary.html', {'form': form, 'summary': str(output_summary.result), 'emailform': form_feedback})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShortTextForm()
        form_feedback = ContactForm()
    return render(request, 'summary_index/summary.html', {'form': form, 'emailform': form_feedback})


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            input_user = form.cleaned_data['user_name']
            input_email = form.cleaned_data['user_email']
            input_message = form.cleaned_data['user_message']
            UserFeedBack.objects.create(user_name=input_user, user_email=input_email, user_message=input_message)
            return render(request, 'summary_index/thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'summary_index/about.html', {'emailform': form})


def test(request):
    return render(request, 'summary_index/generic.html')


def user_info(request):
    ip_addr = request.META['REMOTE_ADDR']

    user_obj = UserInfo.objects.filter(ip=ip_addr)
    if not user_obj:
        UserInfo.objects.create(ip=ip_addr)

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
