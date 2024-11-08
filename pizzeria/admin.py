from django.contrib import admin

from .models import TipoMasa, Ingrediente, Pizza

# Register your models here.

admin.site.register(TipoMasa)
admin.site.register(Ingrediente)
admin.site.register(Pizza)
