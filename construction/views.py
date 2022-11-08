from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'construction/home.html')

def contact(request):
    return HttpResponse('Contato')

def about(request):
    return HttpResponse ('Sobre a Sorroche Engenharia')