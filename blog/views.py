from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from.models import Project1
p=Project1.objects.all()
def blo(request):
    return render(request,'blog.html',{'q':p})
# Create your views here.
 
def detail(request,blog):
    x=get_object_or_404(Project1,pk=blog)
    return render(request,'detail.html',{'y':x})
    


 