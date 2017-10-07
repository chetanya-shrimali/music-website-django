# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Record, Song

admin.site.register(Record)
admin.site.register(Song)
