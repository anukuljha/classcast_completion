# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class courseblock_index(models.Model):
	block_id=models.CharField(primary_key=True,max_length=100)
	course_id=models.CharField(max_length=150)
	block_type=models.CharField(max_length=20)
	block_number=models.IntegerField(default=1)

	class Meta:
		unique_together=('course_id','block_number')

	def __str__(self):
		return self.course_id+str(self.block_number)

class user_block_interaction(models.Model):
	user=models.ForeignKey(User) #change this to foreign key for production
	block=models.ForeignKey(courseblock_index)
	block_number=models.IntegerField(default=0)
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username+str(self.block_number)
