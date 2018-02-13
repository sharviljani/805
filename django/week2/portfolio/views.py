from django.shortcuts import render

def home(request):
	'''
	Renders Home Page
	'''
	context = {} 
	return render(request, 'home.html', context)

def resume(request):

	context = {}
	return render(request, 'resume.html', context)

def portfolio(request):

	context = {}
	return render(request, 'portfolio.html', context)

def contact(request):

	context = {}
	return render(request, 'contact.html', context)