from django.contrib import admin
from .models import Categoria

# Register your models here.

class AdminCategoria(admin.ModelAdmin):
    list_display= ('nombre',)

admin.site.register(Categoria, AdminCategoria)