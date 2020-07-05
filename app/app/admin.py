#-*- coding: utf-8 -*-

from django.contrib import admin
from app.models import Databases

class DatabasesAdmin(admin.ModelAdmin):
	list_display = ('alias', 'host', 'port', 'sid', 'restorepoint')
	list_filter = ('alias',)
	ordering = ('alias',)
	search_fileds = ('alias',)

admin.site.register(Databases, DatabasesAdmin)	