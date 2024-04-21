from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.br.forms import BRCPFField


# CRIAÇÃO DA TABELA VOLUNTARIADO NO BANDO DE DADOS

#criaremos um campo STATUS

STATUS = (
    ('p', 'Pendente'),
    ('a', 'Aprovado'),
    ('r', 'Recusado'),
)

OUTROS = (
    ('s', 'Sim'),
    ('n', 'Não'),
)

class Adotantes(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    celular = PhoneNumberField()
    endereço = models.CharField(max_length=200)
    cpf = models.CharField(max_length=50)
    motivo = models.CharField(max_length=50)
    motivo = models.CharField(max_length=50)
    outros_animais = models.CharField(max_length=3, choices=OUTROS)
    interessado = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)
    status = models.CharField(max_length=1, choices=STATUS, default="p")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Formulário adotante'
        verbose_name_plural = 'Formulários adotantes'
