from django.shortcuts import render
from app_usuarios.forms import UsuariosForms

# Create your views here.
def usuario (request):
    if request.method =='POST': #se o methodo requisitado for IGUAL A POST
        form = UsuariosForms(request.POST) #ele vai puxar o dados do formularios em forms
        if form.is_valid(): #se o formulario for valido
            form.save() #o formulario será salvo
    else: #caso o metodo requisitado não seja POST (ou seja, GET)
        form = UsuariosForms()
    return render(request, 'usuario.html', {'form': form})