from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def service(request):
    return render(request,"main/service.html")

def project(request):
    return render(request,"main/project.html")

def contact(request):
    return render(request,"main/contact.html")