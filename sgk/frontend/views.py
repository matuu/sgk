#encoding=utf-8
from datetime import datetime, timedelta

from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from core.models import Turno, Paciente, Persona, MotivoConsulta, Objetivo, Antecedente
from frontend.forms import TurnoForm, PacienteForm, PersonaForm


class Index(TemplateView):
    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["form_turno"] = TurnoForm()
        return context


class TurnosListView(ListView):
    # queryset = Turno.objects.all()
    #template_name = "frontend/turno_list.html"

    def get_queryset(self):
        dt = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        dt_limit = dt + timedelta(days=7)
        return Turno.objects\
            .filter(dia__gte=dt, dia__lt=dt_limit).order_by('dia', 'hora')


class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    #template_name = 'frontend/turno_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Turno creado correctamente.")
        return reverse_lazy('turno_list')


class TurnoEditView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'frontend/turno_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Turno actualizado correctamente.")
        return reverse_lazy('turno_list')


class PacienteListView(ListView):
    template_name = "frontend/paciente_list.html"

    def get_queryset(self):
        return Paciente.objects.all()


class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    #template_name = 'frontend/paciente_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Paciente creado correctamente.")
        return reverse_lazy('paciente_list')


class PacienteEditView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    #template_name = 'frontend/paciente_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Paciente actualizado correctamente.")
        return reverse_lazy('paciente_list')


class PersonaListView(ListView):
    template_name = "frontend/persona_list.html"

    def get_queryset(self):
        return Persona.objects.all()


class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Persona creada correctamente.")
        return reverse_lazy('persona_list')


class PersonaEditView(UpdateView):
    model = Persona
    form_class = PersonaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Persona actualizada correctamente.")
        return reverse_lazy('persona_list')


class MotivoConsultaListView(ListView):

    def get_queryset(self):
        return MotivoConsulta.objects.all()


class MotivoConsultaCreateView(CreateView):
    model = MotivoConsulta
    #form_class = PersonaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Motivo de consulta creado correctamente.")
        return reverse_lazy('motivo_consulta_list')


class MotivoConsultaEditView(UpdateView):
    model = MotivoConsulta
    #form_class = PersonaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Motivo de Consulta actualizado correctamente.")
        return reverse_lazy('motivo_consulta_list')


class ObjetivoListView(ListView):

    def get_queryset(self):
        return Objetivo.objects.all()


class ObjetivoCreateView(CreateView):
    model = Objetivo
    #form_class = PersonaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Motivo de consulta creado correctamente.")
        return reverse_lazy('objetivo_list')


class ObjetivoEditView(UpdateView):
    model = Objetivo
    #form_class = PersonaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Motivo de Consulta actualizado correctamente.")
        return reverse_lazy('objetivo_list')


class AntecedenteListView(ListView):

    def get_queryset(self):
        return Antecedente.objects.all()


class AntecedenteCreateView(CreateView):
    model = Antecedente
    #form_class = PersonaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Antecedente creado correctamente.")
        return reverse_lazy('antecedente_list')


class AntecedenteEditView(UpdateView):
    model = Antecedente
    #form_class = PersonaForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Antecedente actualizado correctamente.")
        return reverse_lazy('antecedente_list')


index = Index.as_view()
turno_list = TurnosListView.as_view()
turno_create = TurnoCreateView.as_view()
turno_update = TurnoEditView.as_view()
paciente_list = PacienteListView.as_view()
paciente_create = PacienteCreateView.as_view()
paciente_update = PacienteEditView.as_view()
persona_list = PersonaListView.as_view()
persona_create = PersonaCreateView.as_view()
persona_update = PersonaEditView.as_view()
motivo_consulta_list = MotivoConsultaListView.as_view()
motivo_consulta_create = MotivoConsultaCreateView.as_view()
motivo_consulta_update = MotivoConsultaEditView.as_view()
objetivo_list = ObjetivoListView.as_view()
objetivo_create = ObjetivoCreateView.as_view()
objetivo_update = ObjetivoEditView.as_view()
antecedente_list = AntecedenteListView.as_view()
antecedente_create = AntecedenteCreateView.as_view()
antecedente_update = AntecedenteEditView.as_view()