from django.shortcuts import render

def home(request):
	'''
	Renders Home Page
	'''
	context = {} 
	return render(request, 'home.html', context)

def resume(request):
	'''
	Renders the resume page
	'''

	context = {}
	return render(request, 'resume.html', context)

def portfolio(request):
	'''
	Renders the Portfolio Page
	'''

	context = {}
	return render(request, 'portfolio.html', context)

def contact(request):
	'''
	Renders Contact Page
	'''

	context = {}
	return render(request, 'contact.html', context)