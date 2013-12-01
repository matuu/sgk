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
    observaciones = models.TextField(u'Observaciones', blank=True)

    class Meta:
        verbose_name = u"contacto"
        verbose_name_plural = u"contactos"

    def __unicode__(self):
        return u"{} {}".format(
                self.nombre, self.apellido)


class Profesion(BaseModel):
    """
    Representa un profesión cualquiera.
    La profesión del paciente es un dato importante a la hora de diagnosticar
    un paciente.

    """
    nombre = models.CharField(u'Nombre de la profesión', max_length=255, unique=True)
    observaciones = models.TextField(u'Observaciones', blank=True)
    # Luego será completada esta clase

    def __unicode__(self):
        return u"{}".format(self.nombre)

    class Meta:
        verbose_name = u"profesión"
        verbose_name_plural = u"profesiones"


class Persona(BaseModel):
    """
    Una persona del sistema.

    Contiene los datos de un paciente, un profesional
    o cualquier otra persona.

    """
    nombre = models.CharField(u'Nombre', max_length=255)
    apellido = models.CharField(u'Apellido', max_length=255)
    fecha_nacimiento = models.DateField(u'Fecha de nacimiento', help_text="DD/MM/AAAA")
    estado_civil = models.CharField(u'Estado civíl', max_length=255, default=u'soltero')
    dni = models.IntegerField(u'DNI')
    domicilio = models.CharField(u'Domicilio', max_length=255, blank=True)
    observaciones = models.TextField(u'Observaciones', blank=True)
    # relaciones
    contacto = models.ForeignKey(Contacto, verbose_name=u'Contacto', null=True)
    profesion = models.ForeignKey(Profesion, verbose_name=u'Profesión', null=True)

    def __unicode__(self):
        return u"{} {}".format(
                self.nombre, self.apellido)

    class Meta:
        verbose_name = u"persona"
        verbose_name_plural = u"personas"


class Profesional(BaseModel):
    """
    Profesional que trabaja en el lugar,
    el cual puede tomar turnos y pacientes.

    """
    persona = models.ForeignKey(Persona, verbose_name=u'Persona')
    observaciones = models.TextField(u'Observaciones', blank=True)

    def __unicode__(self):
        return u"{}".format(
                self.persona.nombre)

    class Meta:
        verbose_name = u"profesional"
        verbose_name_plural = u"profesionales"


class ObraSocial(BaseModel):
    """
    Representa una obra social o mutual.

    """
    nombre = models.CharField(u'Nombre', max_length=255)
    codigo = models.CharField(u'Código', max_length=255, blank=True)
    telefono = models.CharField(u'Teléfono', max_length=25, blank=True)
    fax = models.CharField(u'fax', max_length=25, blank=True)
    email = models.EmailField(u'E-mail', blank=True)
    contacto = models.ForeignKey(Contacto, verbose_name=u'Contacto', null=True, related_name='obrasocial')


class Paciente(BaseModel):
    """
    Persona que se atiende en el lugar.

    """
    persona = models.ForeignKey(Persona, verbose_name=u'Persona')
    peso = models.DecimalField(u'Peso (Kg)', max_digits=5, decimal_places=2, null=True)
    altura = models.DecimalField(u'Altura (Mts)', max_digits=5, decimal_places=2, null=True)
    fecha_ingreso = models.DateField(u'Fecha de ingreso', help_text="DD/MM/AAAA")
    observaciones = models.TextField(u'Observaciones', blank=True)
    #relaciones
    obra_social = models.ForeignKey(ObraSocial, verbose_name=u'Obra Social', null=True)

    def __unicode__(self):
        return u"{}".format(
                self.persona.nombre)

    class Meta:
        verbose_name = u"paciente"
        verbose_name_plural = u"pacientes"


class Turno(BaseModel):
    """
    """
    dia = models.DateField(u'Día', auto_now_add=True)
    hora = models.TimeField(u'Hora', auto_now_add=True)
    duracion = models.TimeField(u'Duración',
            help_text=u"Duración en horas de la sesión.")
    motivo = models.CharField(u'Motivo', max_length=255, blank=True)
    asistio = models.BooleanField(u'¿Asistió?', default=False)
    aviso = models.BooleanField(u'¿Avisó?')
    observaciones = models.TextField(u'Observaciones', blank=True)
    # relaciones
    profesional = models.ForeignKey(Profesion, verbose_name=u'Profesional')
    paciente = models.ForeignKey(Paciente, verbose_name=u'Paciente', null=True)

