#-*- coding: utf-8 -*-

from django.db import models
from rest_framework import serializers

class Databases(models.Model):

	class Meta:
		verbose_name = 'Database'
		verbose_name_plural = 'Databases'

	alias = models.CharField(max_length=32, unique=True)
	host = models.CharField(max_length=32)
	port = models.IntegerField()
	sid = models.CharField(max_length=32)
	restorepoint = models.CharField(max_length=32)

	def __str__(self):
		return self.alias

class DatabasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Databases
        fields = ('alias', 'host', 'port', 'sid', 'restorepoint')

