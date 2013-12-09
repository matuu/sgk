# coding=utf-8
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.template import loader
from django.utils.http import int_to_base36

from .email import send_html_mail


class HtmlEmailPasswordResetForm(PasswordResetForm):
    """
    This just overrides the default save method to send the email as HTML
    """
    def save(self, domain_override=None,
             subject_template_name='auth_registro/password_reset_subject.txt',
             email_template_name='auth_registro/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        for user in self.users_cache:
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': int_to_base36(user.id),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': use_https and 'https' or 'http',
            }
            subject = loader.render_to_string(subject_template_name, c)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            send_html_mail(subject, email_template_name, c, settings.DEFAULT_FROM_EMAIL, to=[user.email])
