import email
from django.shortcuts import render
from .models import Contact

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            remarks=request.POST['remarks']
        )

    
        return render(request, 'contact.html')

    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def categories(request):
    return render(request, 'categories.html')
