from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def validator(self, POSTdata):
		errors = {}
		if len(POSTdata['name']) < 5:
			errors['name'] = 'ERROR: name must be at least 5 characters long'
		if len(POSTdata['desc']) < 15:
			errors['desc'] = 'ERROR: description must be at least 15 characters long'
		return errors


class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length = 2000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = CourseManager()