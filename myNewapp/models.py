
from django.db import models

# Create your models here.

class student(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()

    class Meta:
        verbose_name_plural="student_dtails"
    def __str__(self):
        return self.name+" "+str(self.age)
