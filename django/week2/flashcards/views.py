from django.shortcuts import render
from .models import Deck

# Create your views here.

def home(request):
	'''
	'''
	qs = Deck.objects.order_by('-title')
	context = {'decks' : qs}
	return render(request, 'flashcards/home.html', context)