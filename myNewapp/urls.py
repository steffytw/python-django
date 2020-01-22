from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('display/',views.display,name = 'display'),
    path('details/<id>',views.details,name = 'details'),
    path('createdata/',views.createdata,name = 'createdata'),
    path('createstudent/',views.createstudent,name = 'createstudent'),
]