from django.shortcuts import render
from app_voluntarios.forms import VoluntariosForms

# Create your views here.
def voluntarios (request):
    if request.method =='POST': #se o methodo requisitado for IGUAL A POST
        form = VoluntariosForms(request.POST) #ele vai puxar o dados do formularios em forms
        if form.is_valid(): #se o formulario for valido
            form.save() #o formulario será salvo
    else: #caso o metodo requisitado não seja POST (ou seja, GET)
        form = VoluntariosForms()
    return render(request, 'voluntarios.html', {'form': form})

