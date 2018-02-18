from django.shortcuts import render
from .models import Education, Experience

# Create your views here.
def home(request):
	'''
	Renders the Resume Home template 
	'''
	exp_qs = Experience.objects.all()
	edu_qs= Education.objects.all()
	context = {'Experience' : exp_qs, 'Education' : edu_qs, 'resume':'active'}
	return render(request,'resume/home.html',context)