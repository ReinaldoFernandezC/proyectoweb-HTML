from django.shortcuts import render, HttpResponse

# Create your views here.

def bienvenida(request):
    return HttpResponse("<h1> Hello World </h1>" )