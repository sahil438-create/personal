from django.http.response import HttpResponse
from django.shortcuts import render
from.models import Project

# Create your views here.

def home(request):
    a=Project.objects.all()
    
    
    return render(request,'home.html',{'b':a})
