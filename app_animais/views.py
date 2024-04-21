from django.shortcuts import render

# Create your views here.

def gatos(request):
    return render(request, 'gatos.html') 

def perros(request):
    return render(request, 'perros.html') 
