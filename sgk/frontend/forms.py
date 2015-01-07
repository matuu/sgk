#encoding=utf-8
from django import forms
from django.forms.models import ModelForm, BaseInlineFormSet
from datetimewidget.widgets import DateWidget, TimeWidget

from core.models import (Antecedente, Turno, Paciente, Objetivo,
                         Persona, ObraSocial, Contacto, MotivoConsulta)


class TurnoForm(ModelForm):
    paciente = forms.ModelChoiceField(Paciente.objects.all(), required=False)
    dia = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    hora = forms.TimeField(widget=TimeWidget(options={"format": "HH:mm"},
                           usel10n=True, bootstrap_version=3), initial="16:00:00")
    duracion = forms.IntegerField(widget=forms.HiddenInput(), initial=60)

    class Meta:
        model = Turno
        fields = ('dia', 'hora', 'duracion', 'motivo', 'observaciones',
                  'nombre_paciente', 'paciente', 'profesional', )


class PacienteForm(ModelForm):
    obra_social = forms.ModelChoiceField(ObraSocial.objects.all(), required=False)
    fecha_ingreso = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))

    class Meta:
        model = Paciente
        fields = ('peso', 'altura', 'fecha_ingreso', 'obra_social',
                  'observaciones')


class PersonaForm(ModelForm):
    fecha_nacimiento = forms.DateField(widget=DateWidget(
        usel10n=True, bootstrap_version=3), initial="01/01/1980")

    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'dni', 'fecha_nacimiento', 'genero', 'estado_civil',
                  'domicilio', 'imagen_perfil')


class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields = ('telefono', 'celular', 'email', 'horario')


class AntecedenteForm(ModelForm):
    menarca = forms.DateField(required=False)
    fum = forms.DateField(required=False)

    class Meta:
        model = Antecedente
        fields = ('patologicos', 'quirurgicos', 'traumaticos', 'alergicos',
                  'heredo_familiar', 'habitos_fisiologicos', 'habitos_patologicos',
                  'medicaciones', 'estudios_complementarios', 'menarca', 'fum',
                  'tipo_partos', 'observaciones')


class MotivoConsultaForm(ModelForm):
    fecha_alta = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))

    class Meta:
        model = MotivoConsulta
        fields = ('id','motivo_consulta_paciente', 'diagnostico_medico', 'evaluacion_kinesica',
                  'cantidad_sesiones', 'tratamientos_previos', 'fecha_alta', 'observaciones')


class ObjetivoInlineForm(BaseInlineFormSet):
    fecha_inicio = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), required=False)
    fecha_cumplido = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), required=False)

    class Meta:
        model = Objetivo
        fields = ('descripcion', 'fecha_inicio', 'fecha_cumplido', 'observaciones')