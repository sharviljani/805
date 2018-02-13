#flashcards url config

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
]
