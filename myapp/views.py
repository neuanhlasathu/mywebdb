from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Student

# Create your views here.
def home(request):
    rs = Student.objects.all()
    context = {
        'rs' :rs
    }
    return render(request,'product/List product.html',context)