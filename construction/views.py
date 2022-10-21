from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME 1')

def contact(request):
    return HttpResponse('Contato')

def about(request):
    return HttpResponse ('Sobre a Sorroche Engenharia')