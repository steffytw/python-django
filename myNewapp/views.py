from django.shortcuts import render
from django.http import HttpResponse
from . models import  student
from . forms import studentForm

# Create your views here.

def home(request):
	context = "HELLO EVERYONE"
	return render(request,'myNewapp/home.html',{'content':context})

def display(request):
	students = student.objects.all()
	return render(request,'myNewapp/display.html',{'students':students})

def details(request,id):
	students_details = student.objects.get(id=id)
	return render(request,'myNewapp/details.html',{'student_detail':students_details})

def createdata(request):
	# student1 = student(name="Rema Venu",age = 37 , address = "HOUSE NO 245,T K NAGAR ,BIHAR")
	# student1.save()
	# student1 = student()
	# student1.name="AYRA YASH"
	# student1.age = 1
	# student1.address="YASH NAGAR,ROCKY BHAI,MUMBAI"
	# student1.save()
	
	# student1 = student.objects.create(name="Rajath Ram",age = 22 , address = "HOUSE NO 245,T K NAGAR ,BIHAR")
	student1 = student.objects.get(id=1)
	student1.delete()
	return HttpResponse("deleted from database")

	# student1.name="Reshma alan"
	# student1.save()
	# return HttpResponse("saved data to database")

def createstudent(request):
	form =studentForm()
	return render(request,'myNewapp/studentform.html',{'form':form})
