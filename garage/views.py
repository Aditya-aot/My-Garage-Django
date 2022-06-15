from django.shortcuts import render

# Create your views here.


def welcome(request) :

    context = {}
    return render(request, 'garage/welcome.html',context)


def home(request) :

    context = {}
    return render(request, 'garage/home.html',context)






