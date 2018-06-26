# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Posts, Incidents
#from forms import ContactForm

admin.site.register(Posts)
admin.site.register(Incidents)
#admin.site.register(ContactForm)