# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from learning_logs.models import Topic
from learning_logs.models import Entry


from django.contrib import admin


# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)
