#encoding=utf-8
from django.views.generic import TemplateView, ListView

from core.models import Turno


class Index(TemplateView):
    template_name = "frontend/index.html"


class TurnosListView(ListView):
    queryset = Turno.objects.all()
    template_name = "frontend/turno_list.html"


index = Index.as_view()
turno_list = TurnosListView.as_view()
