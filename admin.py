# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import courseblock_index, user_block_interaction

# Register your models here.
admin.site.register(courseblock_index)
admin.site.register(user_block_interaction)