from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'basic_app_four/index.htm')

def other(request):
    return render(request,'basic_app_four/other.htm')

def relative(request):
    return render(request,'basic_app_four/relative.htm')

def base(request):
    return render(request,'basic_app_four/base.htm')