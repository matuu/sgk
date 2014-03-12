#encoding=utf-8
from django import forms
from django.forms.models import ModelForm

from core.models import Turno, Paciente


class TurnoForm(ModelForm):
    paciente = forms.ModelChoiceField(Paciente.objects.all(), required=False)

    class Meta:
        model = Turno
        fields = ('dia', 'hora', 'duracion', 'motivo', 'observaciones',
                  'nombre_paciente', 'paciente', 'profesional', )
