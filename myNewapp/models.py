
from django.db import models

# Create your models here.

class student(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()

    class Meta:
        verbose_name_plural="student_details"
    def __str__(self):
        return self.name+" "+str(self.age)


class signupformsData(models.Model):

    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    screenname= models.CharField(max_length=20)
    address = models.TextField()
    password = models.CharField(max_length=50)
    confirmpassword = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural="SignUp_User_Details"
    def __str__(self):

        return self.name
