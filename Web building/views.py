from django.shortcuts import render
from django.shortcuts import HttpResponse
import logging
from gensim.summarization import summarize

# Create your views here.

summarization=None

def index(request):
    if request.method =="POST":
        global summarization
        summarization=request.POST.get("text",None)
        summarization=summarize(summarization)
        print(summarization)
    return render(request,"index.html",{'summarization':summarization})
