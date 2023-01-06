from django.contrib import admin
from .models import *

class koordinatadmin(admin.ModelAdmin):
    list_display = ['nama_cafe', 'alamat', 'koordinat']
    search_fields = ['nama_cafe']
    list_per_page = 5

class menuadmin(admin.ModelAdmin):
    list_display = ['nama_menu']
    search_fields = ['harga']
    list_per_page = 5

admin.site.register(Koordinat, koordinatadmin)
admin.site.register(Menu, menuadmin)


# Register your models here.
