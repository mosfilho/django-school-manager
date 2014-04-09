from django.contrib import admin
from models import Tipo_Conteudo, Conteudo, Galeria_Imagem, Imagem

class ImagemAdmin(admin.StackedInline):
    model = Imagem

class GaleriaImagemAdmin(admin.ModelAdmin):
    inlines = [ImagemAdmin,] 

# Register your models here.
admin.site.register(Galeria_Imagem, GaleriaImagemAdmin)
admin.site.register(Tipo_Conteudo)
admin.site.register(Conteudo)
