from django.contrib import admin
from .models import Persona
from .models import Domicilio

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)
