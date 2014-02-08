#encoding=utf-8
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse_lazy

from core.models import Turno
from frontend.forms import TurnoForm


class Index(TemplateView):
    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["form_turno"] = TurnoForm()
        return context


class TurnosListView(ListView):
    queryset = Turno.objects.all()
    template_name = "frontend/turno_list.html"


class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'frontend/turno_create.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                u"Turno creado correctamente.")
        return reverse_lazy('turno_list')


index = Index.as_view()
turno_list = TurnosListView.as_view()
turno_create = TurnoCreateView.as_view()
