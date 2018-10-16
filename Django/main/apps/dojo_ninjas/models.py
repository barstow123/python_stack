from __future__ import unicode_literals
from django.db import models


# Create your models here.
class dojo(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	desc = models.CharField(max_length=255)

	def __str__(self):
		return f'{self.name}'

	def __repr__(self):
		return f'dojo(name={self.name}, city={self.city}, state={self.state}, created_at={self.created_at}, updated_at={self.aupdated_at})'

class ninja(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dojo = models.ForeignKey(dojo, related_name='ninja')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	def __repr__(self):
		return f'ninja(first_name={self.first_name}, last_name={self.last_name}, dojo={self.dojo}, created_at={self.created_at}, updated_at={self.updated_at})'