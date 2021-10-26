from django.http.response import HttpResponse
from django.shortcuts import render



def homeview(request):
    return render(request, 'home/home.html' )