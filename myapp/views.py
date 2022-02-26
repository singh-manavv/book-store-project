from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
    
def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

def categories(request):
    return render(request,'categories.html')
