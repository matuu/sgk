#encoding=utf-8
from django import forms
from django.forms.models import ModelForm

from core.models import Turno, Paciente, Persona, ObraSocial, Contacto

class TurnoForm(ModelForm):
    paciente = forms.ModelChoiceField(Paciente.objects.all(), required=False)

    class Meta:
        model = Turno
        fields = ('dia', 'hora', 'duracion', 'motivo', 'observaciones',
                  'nombre_paciente', 'paciente', 'profesional', )


class PacienteForm(ModelForm):
    persona = forms.ModelChoiceField(Persona.objects.all(), required=True)
    obra_social = forms.ModelChoiceField(ObraSocial.objects.all(), required=False)

    class Meta:
        model = Paciente
        fields = ('persona', 'peso', 'altura', 'fecha_ingreso', 'obra_social',
                  'observaciones', )


class PersonaForm(ModelForm):
    contacto = forms.ModelChoiceField(Contacto.objects.all(), required=False)

    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'fecha_nacimiento', 'genero', 'estado_civil',
                  'dni', 'domicilio', 'contacto', 'profesion', 'observaciones')
