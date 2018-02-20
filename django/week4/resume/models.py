from django.db import models

# Create your models here.

class Resume(models.Model):
	First_name = models.CharField(max_length=255, null=False, blank=False)
	Last_name = models.CharField(max_length=255, null=False, blank=False)

	def get_full_name(self):
		"""
		returns full name as "Firstname Lastname"
		"""
		return "{} {}".format(self.First_name, self.Last_name)

	def get_last_name_first_name(self):
		"""
		returns full name as "Lastname, Firstname"
		"""
		return "{}, {}".format(self.Last_name, self.First_name)

	def get_education(self):
		"""
		returns education for "Full name" in education table
		"""
		return self.education_set.all()

	def get_experience(self):
		"""
		returns experience for "Full name" in the experience table
		"""
		return self.experience_set.all()


class Education(models.Model):
	'''
	foreign key relationship to the “Resume” model.
	'''
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)
	
	institution_name = models.CharField(max_length=255, null=False, blank=False)
	location = models.CharField(max_length=255, null=False, blank=False)
	degree = models.CharField(max_length=255, null=False, blank=False)
	major = models.CharField(max_length=255, null=False, blank=False)
	gpa = models.FloatField()

	def __str__(self):
		return "{}, {}, {}, {}, {}".format(self.institution_name, self.location,
				self.degree, self.major, self.gpa)


class Experience(models.Model):

	'''
	foreign key relationship to the “Resume” model.
	'''
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default=1)

	title = models.CharField(max_length=255, null=False, blank=False)
	location = models.CharField(max_length=255, null=False, blank=False)
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.CharField(max_length=255, null=False, blank=True)
	
	def __str__(self):
		return "{}, {}, {}, {}, {}".format(self.title, self.location,
			self.start_date, self.end_date, self.description)

