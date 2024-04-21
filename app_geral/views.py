from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def sugestão(request):
    return render(request, 'sugestão.html')

def sucesso(request):
    return render(request, 'sucesso.html')
