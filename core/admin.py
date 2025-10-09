from django.contrib import admin
from .models import Medico, Paciente, Especialidade

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Especialidade)
