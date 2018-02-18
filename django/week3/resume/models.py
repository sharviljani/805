from django.db import models

# Create your models here.

class Education(models.Model):
	institution_name = models.CharField(max_length=255, null=False, blank=False)
	location = models.CharField(max_length=255, null=False, blank=False)
	degree = models.CharField(max_length=255, null=False, blank=False)
	major = models.CharField(max_length=255, null=False, blank=False)
	gpa = models.FloatField()


	def __str__(self):
		return "{}, {}, {}, {}, {}".format(self.institution_name, self.location,
				self.degree, self.major, self.gpa)


class Experience(models.Model):
	title = models.CharField(max_length=255, null=False, blank=False)
	location = models.CharField(max_length=255, null=False, blank=False)
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.CharField(max_length=255, null=False, blank=True)
	
	def __str__(self):
		return "{}, {}, {}, {}, {}".format(self.title, self.location,
			self.start_date, self.end_date, self.description)