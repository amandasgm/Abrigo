from django.shortcuts import render, redirect
from app_voluntarios.forms import VoluntariosForms

# Create your views here.
def voluntarios (request):
    contexto = {}
    sucesso = False
    if request.method =='POST': #se o methodo requisitado for IGUAL A POST
        form = VoluntariosForms(request.POST) #ele vai puxar o dados do formularios em forms
        if form.is_valid(): #se o formulario for valido
            form.save() #o formulario será salvo
            sucesso = True
    else: #caso o metodo requisitado não seja POST (ou seja, GET)
        form = VoluntariosForms()
    
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }

    return render(request, 'voluntarios.html', contexto)

def sucesso(request):
    return render(request, 'sucesso.html')