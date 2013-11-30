# -*- coding: utf-8 -*-
from django.db import models


class BaseModel(models.Model):
    """
    Todos los modelos deben heredar de esta clase.

    """
    class Meta:
        abstract = True

    creado_el = models.DateTimeField(verbose_name=u"Fecha de creación",
            auto_now_add=True)
    modificado_el = models.DateTimeField(verbose_name=u"Fecha de modificación",
            auto_now=True)


class Contacto(BaseModel):
    """
    Representa un contacto.

    Puede ser los datos de contacto de un paciente, un profesional,
    o otra persona relacionado con el sistema.

    """
    nombre = models.CharField(u'Nombre', max_length=255, blank=True)
    apellido = models.CharField(u'Apellido', max_length=255, blank=True)
    telefono = models.CharField(u'Teléfono', max_length=255, blank=True)
    celular = models.CharField(u'Celular', max_length=255, blank=True)
    email = models.EmailField(u'E-mail', blank=True)
    horario = models.CharField(u'Horario de contacto', max_length=255, blank=True)
    observaciones = models.TextField()


class Profesion(BaseModel):
    """
    Representa un profesión cualquiera.
    La profesión del paciente es un dato importante a la hora de diagnosticar
    un paciente.

    """
    nombre = models.CharField(u'Nombre de la profesión', max_length=255)
    observaciones = models.TextField()
    # Luego será completada esta clase.


class Persona(BaseModel):
    """
    Una persona del sistema.

    Contiene los datos de un paciente, un profesional
    o cualquier otra persona.

    """
    nombre = models.CharField(u'Nombre', max_length=255)
    apellido = models.CharField(u'Apellido', max_length=255)
    fecha_nacimiento = models.DateField(u'Fecha de nacimiento', help_text="DD/MM/AAAA")
    estado_civil = models.CharField(u'Estado civíl', max_length=255)
    dni = models.IntegerField(u'DNI')
    domicilio = models.CharField(u'Domicilio', max_length=255, blank=True)
    observaciones = models.TextField()
    # relaciones
    contacto = models.ForeignKey(Contacto, verbose_name=u'Contacto', null=True)
    profesion = models.ForeignKey(Profesion, verbose_name=u'Profesión', null=True)


class Profesional(BaseModel):
    """
    Profesional que trabaja en el lugar,
    el cual puede tomar turnos y pacientes.

    """
    persona = models.ForeignKey(Persona, verbose_name=u'Persona')
    observaciones = models.TextField()


class Paciente(BaseModel):
    """
    Persona que se atiende en el lugar.

    """
    persona = models.ForeignKey(Persona, verbose_name=u'Persona')
    peso = models.DecimalField(u'Peso (Kg)', max_digits=5, decimal_places=2, null=True)
    altura = models.DecimalField(u'Altura (Mts)', max_digits=5, decimal_places=2, null=True)
    fecha_ingreso = models.DateField(u'Fecha de ingreso', help_text="DD/MM/AAAA")
    observaciones = models.TextField()

