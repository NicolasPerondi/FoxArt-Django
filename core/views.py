from django.shortcuts import render, HttpResponse

# Create your views here.

def contacto(request):
    return render(request,"core/contacto.html")

def nosotros(request):
    return render(request,"core/nosotros.html")
