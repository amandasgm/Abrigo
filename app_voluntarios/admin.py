
from django.contrib import admin
from app_voluntarios.models import Voluntariado

# Register your models here.
@admin.register(Voluntariado)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'celular', 'endereço', 'cpf', 'profissão']
    search_fields = ['nome', 'email', 'celular', 'endereço', 'cpf', 'profissão']
    list_filter = ['ativo', 'status']