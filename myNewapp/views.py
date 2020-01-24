from django.shortcuts import render
from django.http import HttpResponse
from . models import  student,signupformsData
from . forms import studentForm,signupForm

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
	if request.method == "POST":
		form = studentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("form submitted")
		else:
			return HttpResponse(form.errors)

	return render(request,'myNewapp/studentform.html',{'form':form})


def signup(request):
	form = signupForm()
	if request.method == "POST":
		form = signupForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			username = form.cleaned_data['username']
			screen_name = form.cleaned_data['screen_name']
			address = form.cleaned_data['address']
			password = form.cleaned_data['password']
			confirm_Password = form.cleaned_data['confirm_Password']
			signup1 = signupformsData()
			signup1.name = name
			signup1.username = username
			signup1.screen_name = screen_name
			signup1.address = address
			signup1.password= password
			signup1.confirm_Password = confirm_Password
			signup1.save()
			return HttpResponse("form submitted")
		# else:
		# 	return HttpResponse(form.errors)
	return render(request,'myNewapp/signupform.html',{'form':form})