from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(res):
	return render(res, 'home.html')