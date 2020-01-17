from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	context = "HELLO EVERYONE"
	return render(request,'myNewapp/home.html',{'content':context})
	
