from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
    template = loader.get_template('pages/login.html')
    #return HttpResponse ("Hello world")
    return HttpResponse(template.render())
    
def Register(request):
    template = loader.get_template('pages/Register.html')
    #return HttpResponse ("Hello world")
    return HttpResponse(template.render())
    