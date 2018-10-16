from django.db import models

# Create your models here.
class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.name}'

	def __repr__(self):
		return f'Book(name={self.name}, desc={self.desc}, created_at{self.created_at}, updated_at{self.updated_at})'

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name='authors')
	notes = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	def __repr__(self):
		return f'Author(first_name={self.first_name}, last_name={self.last_name}, email={self.email}, created_at={self.created_at}, updated_at={self.updated_at})'