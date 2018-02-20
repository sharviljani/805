from django.shortcuts import render
from .models import Education, Experience, Resume

# Create your views here.
def home(request):
	'''
	Renders the Resume Home template 
	'''
	exp_qs = Experience.objects.all()
	edu_qs = Education.objects.all()
	res_qs = Resume.objects.first()
	return render(request,'resume/home.html',context={"resume":res_qs})