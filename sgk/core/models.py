# -*- coding: utf-8 -*-
from functools import partial

from django.db import models
from django.contrib.auth.models import User

from utils_sgk.models import BaseModel, uploadFilename


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
    GENERO = (
        ('F', u'Femenino'),
        ('M', u'Masculino'),
        ('O', u'Otro')
    )
    ESTADO_CIVIL = (
        ('S', u"soltero"),
        ('C', u"casado"),
        ('D', u"divorciado"),
        ('V', u"viudo"),
        ('CV', u"Concuvinato")
    )
    nombre = models.CharField(u'Nombre', max_length=255)
    apellido = models.CharField(u'Apellido', max_length=255)
    fecha_nacimiento = models.DateField(u'Fecha de nacimiento', help_text="DD/MM/AAAA")
    genero = models.CharField(u'Género', max_length=1, choices=GENERO, default=u'F')
    estado_civil = models.CharField(u'Estado civíl', max_length=3, choices=ESTADO_CIVIL, default='S')
    dni = models.IntegerField(u'DNI')
    domicilio = models.CharField(u'Domicilio', max_length=255, blank=True)
    imagen_perfil = models.ImageField(upload_to=partial(uploadFilename, 'imagen_perfil'),
                                      blank=True, null=True)
    observaciones = models.TextField(u'Observaciones', blank=True)
    # relaciones
    contacto = models.ForeignKey(Contacto, verbose_name=u'Contacto', null=True, blank=True)
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
    usuario = models.OneToOneField(User, verbose_name=u'Usuario', null=True)
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

    def __unicode__(self):
        return u"{}".format(self.nombre)

    class Meta:
        verbose_name = u"obra social"
        verbose_name_plural = u"obras sociales"


class Antecedente(BaseModel):
    """
    Representa la historia médica del paciente.
    Contiene datos médicos y relevantes sobre el paciente.

    """
    patologicos = models.TextField(u'Patológicos', blank=True)
    quirurgicos = models.TextField(u'Quirúrgicos', blank=True)
    traumaticos = models.TextField(u'Traumáticos', blank=True)
    alergicos = models.TextField(u'Alérgicos', blank=True)
    heredo_familiar = models.TextField(u'Heredo familiar', blank=True)
    habitos_fisiologicos = models.TextField(u'Hábitos fisiológicos', blank=True)
    habitos_patologicos = models.TextField(u'Hábitos patológicos', blank=True)
    medicaciones = models.TextField(u'Medicaciones', blank=True)
    estudios_complementarios = models.TextField(u'Estudios complementarios', blank=True)
    menarca = models.DateField(u'MENARCA', null=True)
    fum = models.DateField(u'FUM', null=True)
    tipo_partos = models.TextField(u'Tipo de partos', blank=True)
    observaciones = models.TextField(u'Observaciones', blank=True)

    def __unicode__(self):
        return u"Antecedentes de {}".format(
                self.paciente.persona)

    class Meta:
        verbose_name = u"antecedente"
        verbose_name_plural = u"antecedentes"


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
    antecedente = models.OneToOneField(Antecedente, verbose_name=u"Antecedente")

    def __unicode__(self):
        return u"{}".format(
                self.persona.nombre)

    class Meta:
        verbose_name = u"paciente"
        verbose_name_plural = u"pacientes"


class Turno(BaseModel):
    """
    """
    dia = models.DateField(u'Día')
    hora = models.TimeField(u'Hora')
    duracion = models.PositiveSmallIntegerField(u'Duración', default=60,
            help_text=u"Duración en minutos de la sesión.")
    motivo = models.CharField(u'Motivo', max_length=255, blank=True)
    asistio = models.BooleanField(u'¿Asistió?', default=False)
    aviso = models.BooleanField(u'¿Avisó?', default=False)
    observaciones = models.TextField(u'Observaciones',  blank=True)
    nombre_paciente = models.CharField(u'Nombre del paciente', max_length=255, blank=True,
            help_text=u'Dejar en blanco si el paciente se encuentra en el sistema.')
    # relaciones
    profesional = models.ForeignKey(Profesional, verbose_name=u'Profesional')
    paciente = models.ForeignKey(Paciente, verbose_name=u'Paciente', null=True)

    def __unicode__(self):
        nombre = u''
        if self.nombre_paciente:
            nombre = self.nombre_paciente
        # elif self.paciente and self.paciente.persona:
        #     nombre = self.paciente.persona.nombre
        else:
            nombre = u"NN"
        return u"{} - {} {} ({})".format(
                nombre, self.dia, self.hora,
                self.profesional.persona.nombre)

    class Meta:
        verbose_name = u"turno"
        verbose_name_plural = u"turnos"


class Antecedente(BaseModel):
    """
    Representa la historia médica del paciente.
    Contiene datos médicos y relevantes sobre el paciente.

    """
    patologicos = models.TextField(u'Patológicos', blank=True)
    quirurgicos = models.TextField(u'Quirúrgicos', blank=True)
    traumaticos = models.TextField(u'Traumáticos', blank=True)
    alergicos = models.TextField(u'Alérgicos', blank=True)
    heredo_familiar = models.TextField(u'Heredo familiar', blank=True)
    habitos_fisiologicos = models.TextField(u'Hábitos fisiológicos', blank=True)
    habitos_patologicos = models.TextField(u'Hábitos patológicos', blank=True)
    medicaciones = models.TextField(u'Medicaciones', blank=True)
    estudios_complementarios = models.TextField(u'Estudios complementarios', blank=True)
    menarca = models.DateField(u'MENARCA', null=True)
    fum = models.DateField(u'FUM', null=True)
    tipo_partos = models.TextField(u'Tipo de partos', blank=True)
    observaciones = models.TextField(u'Observaciones', blank=True)

    def __unicode__(self):
        return u"Antecedentes de {}".format(
                self.paciente.persona.nombre)

    class Meta:
        verbose_name = u"antecedente"
        verbose_name_plural = u"antecedentes"


class MotivoConsulta(BaseModel):
    """
    Contiene información sobre el motivo por el cual
    el paciente debe tomar algunas sesiones.

    """
    motivo_consulta_paciente = models.TextField(
            u'Motivo según el paciente', blank=True, default=u"",
            help_text=u"Signos y síntomas explicados por el paciente.")
    diagnostico_medico = models.TextField(u'Diagnóstico médico',
            help_text=u'Diagnóstico que elaboró el médico especialista.')
    evaluacion_kinesica = models.TextField(u'Evaluación Kinésica',
            help_text=u'Evaluación elaborada por el kinesiólogo/a.')
    fecha_ingreso = models.DateField(u'Fecha de ingreso', auto_now_add=True)
    cantidad_sesiones = models.IntegerField(u'Cantidad de sesiones',
            help_text=u'Cantidad de sesiones necesarias recetadas por el médico.', default=10)
    tratamientos_previos = models.TextField(u'Tratamientos previos', blank=True,
            help_text=u'Descripción de tratamientos previos '
                      u'por el mismo motivo de consulta')
    fecha_alta = models.DateField(u'Fecha de alta', null=True, blank=True,
            help_text=u'Fecha de alta tentativa.')
    observaciones = models.TextField(u'Observaciones', blank=True)
    paciente = models.ForeignKey(Paciente, verbose_name=u'Paciente', related_name='motivos_de_consulta')

    def __unicode__(self):
        if self.evaluacion_kinesica:
            return u"{} - {}".format(
                self.evaluacion_kinesica[:50], self.creado_el.strftime("%d/%m/%Y"))
        elif self.diagnostico_medico:
            return u"{} - {}".format(
                self.diagnostico_medico[:50], self.creado_el.strftime("%d/%m/%Y"))
        else:
            return u"{}".format(
                self.creado_el)

    class Meta:
        verbose_name = u"motivo de consulta"
        verbose_name_plural = u"motivos de consulta"


class Objetivo(BaseModel):
    """
    Representa un objetivo del tratamiento.
    Puede haber varios para un tratamiento, y se van cumpliendo
    con el paso de las sesiones.

    """
    descripcion = models.CharField(u'Descripción', max_length=255)
    fecha_inicio = models.DateField(u'Fecha de inicio', null=True)
    fecha_cumplido = models.DateField(u'Fecha de éxito', null=True)
    observaciones = models.TextField(u'Observaciones', blank=True)
    # relaciones
    motivo_consulta = models.ForeignKey(MotivoConsulta,
            verbose_name=u'Motivo de consulta', null=True)

    def __unicode__(self):
        return u"{}".format(
                self.descripcion)

    class Meta:
        verbose_name = u"objectivo"
        verbose_name_plural = u"objetivos"
