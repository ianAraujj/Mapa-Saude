from django.contrib import admin
from .models import *

class userAdmin(admin.ModelAdmin):
    list_display = ['username', 'nome', 'email', 'categoria', 'is_staff', 'unidade_lotado']
    search_fields = ['username', 'nome']

admin.site.register(User, userAdmin)
admin.site.register(Agravo)
admin.site.register(CategoriaProfissional)
admin.site.register(Estabelecimento)
admin.site.register(Paciente)
admin.site.register(Sinais_Clinicos)
admin.site.register(Doencas_Pre_Existentes)
