# -*- coding: utf-8 -*-

u"""
Defaults and overrides for envelope-related settings.
"""

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


DEFAULT_CONTACT_CHOICES = (
    ('',    _("Choose")),
    (10,    _("A general question regarding the website")),
    (None,  _("Other")),
)

ENVELOPE_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL

ENVELOPE_CONTACT_CHOICES = getattr(settings, 'ENVELOPE_CONTACT_CHOICES',
                                   DEFAULT_CONTACT_CHOICES)

ENVELOPE_EMAIL_RECIPIENTS = getattr(settings, 'ENVELOPE_EMAIL_RECIPIENTS',
                           [settings.DEFAULT_FROM_EMAIL])

ENVELOPE_SUBJECT_INTRO = getattr(settings, 'ENVELOPE_SUBJECT_INTRO',
                                 _("Message from contact form: "))
