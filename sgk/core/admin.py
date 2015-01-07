# -*- coding: utf-8 -*-
from django.contrib import admin
from core.models import (Contacto, Profesion, Profesional, Persona,
                         Paciente, Turno, ObraSocial, MotivoConsulta, Objetivo)

admin.site.register(ObraSocial)
admin.site.register(Turno)
admin.site.register(Contacto)
admin.site.register(Profesion)
admin.site.register(Profesional)
admin.site.register(Persona)
admin.site.register(Paciente)
admin.site.register(MotivoConsulta)
admin.site.register(Objetivo)
