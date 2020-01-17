from django.shortcuts import render
from django.http import HttpResponse
from . models import  student

# Create your views here.

def home(request):
	context = "HELLO EVERYONE"
	return render(request,'myNewapp/home.html',{'content':context})

def display(request):
	students = student.objects.all[:5]
	return render(request,'display.html',{'students':student})


	
