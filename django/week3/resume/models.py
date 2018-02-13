from django.db import models

# Create your models here.

class Education(models.Model):
	institution_name = models.CharField(max_length=255, null=False, blank=False)
	location = models.CharField(max_length=255, null=False, blank=False)
	degree = models.CharField(max_length=255, null=False, blank=False)
	major = models.CharField(max_length=255, null=False, blank=False)
	gpa = models.FloatField(max_length=255, null=False, blank=False)

	def __str__(self):

		"""
		String for representing the Model object.
		"""
		return self.institution_name

class Experience(models.Model):
	title = models.CharField(max_length=255, null=False, blank=False)
	location = models.CharField(max_length=255, null=False, blank=False)
	start_date = models.DateField(max_length=255, null=False, blank=False)
	end_date = models.DateField(max_length=255, null=False, blank=False)
	description = models.CharField(max_length=255, null=False, blank=True)

	def __str__(self):
		return self.title, location, start_date, end_date, description