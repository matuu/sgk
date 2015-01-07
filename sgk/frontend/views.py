#encoding=utf-8
from datetime import datetime, timedelta

from django.contrib import messages
from django.db.models import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from enhanced_cbv.views.edit import InlineFormSetsView, EnhancedInlineFormSet
# from tables_filters.edit import InlineFormSetsView, EnhancedInlineFormSet

from utils_sgk.views import AuthenticatedMixin
from core.models import (Turno, Paciente, Persona, Profesional, Antecedente,
                         MotivoConsulta, Objetivo)
from frontend.forms import (TurnoForm, PacienteForm, PersonaForm,
                            ContactoForm, AntecedenteForm, MotivoConsultaForm, ObjetivoInlineForm)


class Index(AuthenticatedMixin, TemplateView):
    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["form_turno"] = TurnoForm()
        return context


class TurnosListView(AuthenticatedMixin, ListView):
    # queryset = Turno.objects.all()
    #template_name = "frontend/turno_list.html"

    def get_queryset(self):
        dt = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        dt_limit = dt + timedelta(days=14)
        return Turno.objects\
            .filter(dia__gte=dt, dia__lt=dt_limit).order_by('dia', 'hora')


class TurnoCreateView(AuthenticatedMixin, CreateView):
    model = Turno
    form_class = TurnoForm
    #template_name = 'frontend/turno_form.html'

    # def get_form(self, form_class):
    #
    #     form1 = super(TurnoCreateView, self).get_form(form_class)
    #     # (initial={})
    #     return form1

    def get_initial(self):
        try:
            profesional = Profesional.objects.get(usuario=self.request.user)
            self.initial.update({'profesional': profesional})
        except ObjectDoesNotExist:
            pass
        return super(TurnoCreateView, self).get_initial()

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Turno creado correctamente.")
        return reverse_lazy('turno_list')


class TurnoEditView(AuthenticatedMixin, UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'frontend/turno_form.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Turno actualizado correctamente.")
        return reverse_lazy('turno_list')


class PacienteListView(AuthenticatedMixin, ListView):
    template_name = "frontend/paciente_list.html"

    def get_queryset(self):
        return Paciente.objects.all()


class PacienteCreateView(AuthenticatedMixin, CreateView):
    model = Paciente
    form_class = PacienteForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        persona_form = PersonaForm()
        contacto_form = ContactoForm()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  persona_form=persona_form,
                                  contacto_form=contacto_form))

    def get_initial(self):
        hoy = datetime.today()
        self.initial.update({'fecha_ingreso': hoy})
        return super(PacienteCreateView, self).get_initial()

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        persona_form = PersonaForm(self.request.POST, self.request.FILES)
        contacto_form = ContactoForm(self.request.POST)
        if form.is_valid() and persona_form.is_valid()\
                and contacto_form.is_valid():
            return self.form_valid(form, persona_form, contacto_form)
        else:
            return self.form_invalid(form, persona_form, contacto_form)

    def form_valid(self, form, persona_form, contacto_form):
        persona = persona_form.save(commit=False)
        contacto = contacto_form.save(commit=False)
        self.object = form.save(commit=False)
        contacto.nombre = persona.nombre
        contacto.apellido = persona.apellido
        contacto.save()
        persona.contacto = contacto
        persona.save()
        antecedente = Antecedente()
        antecedente.save()
        self.object.antecedente =antecedente
        self.object.persona = persona
        self.object.save()
        motivo = MotivoConsulta()
        motivo.cantidad_sesiones = 10
        motivo.paciente_id = self.object.pk
        motivo.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, persona_form, contacto_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  persona_form=persona_form,
                                  contacto_form=contacto_form))

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Paciente creado correctamente.")
        return reverse_lazy('paciente_list')


class PacienteEditView(AuthenticatedMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        persona_form = PersonaForm(instance=self.object.persona)
        contacto_form = ContactoForm(instance=self.object.persona.contacto)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  persona_form=persona_form,
                                  contacto_form=contacto_form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        persona_form = PersonaForm(self.request.POST, self.request.FILES, instance=self.object.persona)
        contacto_form = ContactoForm(self.request.POST, instance=self.object.persona.contacto)
        if form.is_valid() and persona_form.is_valid()\
                and contacto_form.is_valid():
            return self.form_valid(form, persona_form, contacto_form)
        else:
            return self.form_invalid(form, persona_form, contacto_form)

    def form_valid(self, form, persona_form, contacto_form):
        persona = persona_form.save(commit=False)
        contacto = contacto_form.save(commit=False)
        self.object = form.save(commit=False)
        contacto.nombre = persona.nombre
        contacto.apellido = persona.apellido
        contacto.save()
        persona.contacto = contacto
        persona.save()
        self.object.persona = persona
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, persona_form, contacto_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  persona_form=persona_form,
                                  contacto_form=contacto_form))

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Paciente editado correctamente.")
        return reverse_lazy('paciente_list')


class PersonaListView(AuthenticatedMixin, ListView):
    template_name = "frontend/persona_list.html"

    def get_queryset(self):
        return Persona.objects.all()


class FichaKinesicaEditView(AuthenticatedMixin, InlineFormSetsView):
    """
    El ID dado será del paciente, de debe buscar el antecedente
    """
    template_name = "frontend/ficha_kinesica.html"
    model = Antecedente
    form_class = AntecedenteForm

    class ObjetivoInline(EnhancedInlineFormSet):
        formset_class = ObjetivoInlineForm
        model = Objetivo
        extra = 0
        can_delete = True

    formsets = [ObjetivoInline, ]

    def get_factory_kwargs(self):
        return {
            'parent_model': MotivoConsulta
        }

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        return Paciente.objects.get(pk=pk).antecedente

    def get_motivo_instance(self):
        if self.kwargs.get('motivo_pk', None):
            return self.object.paciente.motivos_de_consulta.get(
                pk=self.kwargs.get('motivo_pk', None))
        else:
            return self.object.paciente.motivos_de_consulta.latest('fecha_ingreso')

    def post(self, request, *args, **kwargs):
        return super(FichaKinesicaEditView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        motivo_form = self.get_motivo_form()
        motivo_form.save()
        return super(FichaKinesicaEditView, self).form_valid(form)

    def get_formsets_kwargs(self, enhanced_formset):
        kwargs = super(FichaKinesicaEditView, self).get_formsets_kwargs(enhanced_formset)
        kwargs.update({
            'instance': self.get_motivo_instance()
        })
        return kwargs

    def get_motivo_form(self):
        if self.request.method == "POST":
            return MotivoConsultaForm(self.request.POST,
                                      instance=self.get_motivo_instance())
        else:
            return MotivoConsultaForm(instance=self.get_motivo_instance())

    def get_context_data(self, *args, **kwargs):
        context = super(FichaKinesicaEditView, self).get_context_data(*args, **kwargs)
        #context["form"] = self.get_form(self.get_form_class())
        context["paciente"] = self.object.paciente
        context["motivo_form"] = self.get_motivo_form()
        context["motivos"] = self.object.paciente.motivos_de_consulta.all()
        return context

    def get_success_url(self, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS,
            u"Ficha editada correctamente.")
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if self.kwargs.get('motivo_pk', None):
            motivo_pk = self.kwargs.get('motivo_pk', None)
            return reverse_lazy('ficha_kinesica',
                                kwargs={'pk': pk,
                                        'motivo_pk': motivo_pk})
        else:
            return reverse_lazy('ficha_kinesica',
                                kwargs={'pk': pk})


index = Index.as_view()
turno_list = TurnosListView.as_view()
turno_create = TurnoCreateView.as_view()
turno_update = TurnoEditView.as_view()
paciente_list = PacienteListView.as_view()
paciente_create = PacienteCreateView.as_view()
paciente_update = PacienteEditView.as_view()
persona_list = PersonaListView.as_view()
ficha_kinesica = FichaKinesicaEditView.as_view()