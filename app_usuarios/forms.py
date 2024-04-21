from django import forms
from app_usuarios.models import Adotantes

class UsuariosForms(forms.ModelForm):
    class Meta:
        model = Adotantes
        fields = ['nome', 'email', 'celular', 'endereço', 'cpf', 'motivo', 'outros_animais', 'interessado']

        def clean(self):
            cleaned_data = super().clean()
            nome = cleaned_data.get('nome')
            email = cleaned_data.get('email')
            celular = cleaned_data.get('celular')
            endereço = cleaned_data.get('endereço')
            cpf = cleaned_data.get('cpf')
            motivo = cleaned_data.get('motivo')
            outros_animais = cleaned_data.get('outros_animais')
            interessado = cleaned_data.get('interessado')


    