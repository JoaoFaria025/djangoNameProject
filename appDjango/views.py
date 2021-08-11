from django.shortcuts import render
from django.http import HttpResponse #import feito

def index(request): #função criada
    return render(request,'index.html')


