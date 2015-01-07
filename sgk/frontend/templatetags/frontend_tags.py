__author__ = 'm4tuu'
# coding=utf-8
from django import template
from django.utils.safestring import mark_safe

from sgk.settings import STATIC_URL

register = template.Library()

@register.filter(name="profile_image")
def profile_image(paciente, classes=None):
    if paciente.persona.imagen_perfil:
        img = paciente.persona.imagen_perfil.url
    else:
        img = STATIC_URL
        if paciente.persona.genero == u'F':
            img += "img/mujer.png"
        elif paciente.persona.genero == u'M':
            img += "img/hombre.png"
        else:
            img += "img/otros.png"
    return mark_safe("<img src='{}' alt='Imágen de perfil' class='{} img-responsive'/>"
                     .format(
            img, classes
        ))

@register.filter(name="split")
def split(str, splitter):
    return str.split(splitter)

