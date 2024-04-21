from django import forms
from app_voluntarios.models import Voluntariado

class VoluntariosForms(forms.ModelForm):
    class Meta:
        model = Voluntariado
        fields = ['nome', 'email', 'celular', 'endereço', 'cpf', 'profissão']

        def clean(self):
            cleaned_data = super().clean()
            nome = cleaned_data.get('nome')
            email = cleaned_data.get('email')
            celular = cleaned_data.get('celular')
            endereço = cleaned_data.get('endereço')
            cpf = cleaned_data.get('cpf')
            profissão = cleaned_data.get('profissão')

    