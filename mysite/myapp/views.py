from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners

def home(request):
    
    return render(request,'home.html')
def check(request):
    x=request.POST['furl']
    shortener=pyshorteners.Shortener()
    link = shortener.tinyurl.short(x)
    print(link)
    return HttpResponse(link)
