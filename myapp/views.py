from django.shortcuts import render
from .models import *

# Create your views here.

def IndexView(request):#view for index.html next configure url
    return render(request,"myapp/index.html")

def htmlform(request):
    return render(request,"myapp/Forms.html")

def InsertPageView(request):
    return render(request,"myapp/insert.html")

def InsertData(request):
    #this part of the code is to get data from HTML to View
    #the fname refers to the name given in the HTML page
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']

    #creating object of model class
    # [please import the models for this using from .models import *]
    #for inserting data

    newuser=Student.objects.create(Firstname=fname,Lasttname=lname,Email=email,Contact=contact)


    #after insertion to redit to show.html
    return render(request,"myapp/show.html")