#encoding=utf-8
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy

from utils_sgk.forms import HtmlEmailPasswordResetForm

urlpatterns = patterns('frontend.views',
    url(r'^$', 'index', name='index'),
    url(r'^turnos/$', 'turno_list', name='turno_list'),
    url(r'^turnos/nuevo$', 'turno_create', name='turno_create'),
    url(r'^turnos/editar/(?P<pk>\d+)/$', 'turno_update', name="turno_update"),
    url(r'^pacientes/$', 'paciente_list', name='paciente_list'),
    url(r'^pacientes/nuevo$', 'paciente_create', name='paciente_create'),
    url(r'^pacientes/editar/(?P<pk>\d+)/$', 'paciente_update', name="paciente_update"),
    url(r'^personas/$', 'persona_list', name='persona_list'),
    url(r'^personas/nuevo$', 'persona_create', name='persona_create'),
    url(r'^personas/editar/(?P<pk>\d+)/$', 'persona_update', name="persona_update"),
    url(r'^motivodeconsulta/$', 'motivo_consulta_list', name='motivo_consulta_list'),
    url(r'^motivodeconsulta/nuevo$', 'motivo_consulta_create', name='motivo_consulta_create'),
    url(r'^motivodeconsulta/editar/(?P<pk>\d+)/$', 'motivo_consulta_update', name="motivo_consulta_update"),
    url(r'^objetivo/$', 'objetivo_list', name='objetivo_list'),
    url(r'^objetivo/nuevo$', 'objetivo_create', name='objetivo_create'),
    url(r'^objetivo/editar/(?P<pk>\d+)/$', 'objetivo_update', name="objetivo_update"),
    url(r'^antecedente/$', 'antecedente_list', name='antecedente_list'),
    url(r'^antecedente/nuevo$', 'antecedente_create', name='antecedente_create'),
    url(r'^antecedente/editar/(?P<pk>\d+)/$', 'antecedente_update', name="antecedente_update"),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'auth_registro/login.html'},
        name='auth_login'),

    url(r'^logout/$', 'logout',
        {'template_name': 'auth_registro/logout.html',
         'next_page': reverse_lazy('frontend.views.index')},
        name='auth_logout'),

    url(r'^password/change/$', 'password_change',
        {'template_name': 'auth_registro/password_change_form.html'},
        name='auth_password_change'),

    url(r'^password/change/done/$', 'password_change_done',
        {'template_name': 'auth_registro/password_change_done.html'},
        name='auth_password_change_done'),

    url(r'^password/reset/$', 'password_reset',
        {
            'template_name': 'auth_registro/password_reset_form.html',
            'email_template_name': 'auth_registro/password_reset_email.html',
            'subject_template_name': 'auth_registro/password_reset_subject.html',
            'post_reset_redirect': reverse_lazy('auth_password_reset_done'),
            'password_reset_form': HtmlEmailPasswordResetForm,
        },
        name='auth_password_reset'),

    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'password_reset_confirm', {
            'template_name':
            'auth_registro/password_reset_confirm.html',
            'post_reset_redirect':
            reverse_lazy('auth_password_reset_complete')},
        name='auth_password_reset_confirm'),

    url(r'^password/reset/complete/$', 'password_reset_complete',
        {'template_name': 'auth_registro/password_reset_complete.html'},
        name='auth_password_reset_complete'),

    url(r'^password/reset/done/$', 'password_reset_done',
        {'template_name': 'auth_registro/password_reset_done.html'},
        name='auth_password_reset_done'),
)

