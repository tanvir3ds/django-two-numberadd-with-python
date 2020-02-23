from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html", {'name':'Tanvir'})

def add(request):
    num1 = int( request.POST['number1'])
    num2= int( request.POST['number2'])

    result = num1 + num2

    return render(request, "result.html",{'res': result} )
