from django.test import TestCase

from datetime import date # for dates in Experience

from .models import Education, Experience, Resume

# Create your tests here.
class ResumeTest(TestCase):
	'''
		Tests the cases shown below
	'''

	resume = Resume(First_name="Sharvil", Last_name="Jani")
	education = Education(institution_name = "UNH", location = "Manchester, NH", degree = "MS", 
		major = "IT", gpa = 3.8)
	experience = Experience(title = "QA Team Lead", location = "Rochester NH", 
		start_date = "2016-08-15", end_date = date.today(), description = "Quality Assurance")

	def setUp(self):
		self.resume.save()
		self.education.save()
		self.experience.save()

	def test_get_full_name(self):
		"""
		Tests get_full_name method of Resume model
		"""
		self.assertEqual(self.resume.get_full_name(), "Sharvil Jani")

	def test_get_last_name_first_name(self):
		"""
		Tests get_last_name_first_name method of Resume model
		"""
		self.assertEqual(self.resume.get_last_name_first_name(), "Jani, Sharvil")

	def test_get_experience(self):
		"""
		Tests get_experience method of Resume model
		"""
		self.assertEqual(self.resume.get_experience().first(), self.experience)

	def test_get_education(self):
		"""
		Tests get_education method of Resume model
		"""
		self.assertEqual(self.resume.get_education().first(), self.education)