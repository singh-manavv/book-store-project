import email
from django.shortcuts import render
from .models import Contact, User

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
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
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Emial Already Registered"
            return render(request,'signup.html',{'msg':msg})

        except:
            if request.POST['password']==request.POST['cpassword']:
                
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                    cpassword=request.POST['cpassword'],
                    address=request.POST['address']
                    )
                msg="User Signup Successfully"
                print(msg)
                return render(request, 'signin.html',{'msg':msg})
            else:
                msg="Password & Confirm Password Does Not Matched"
                return render(request, 'signup.html',{'msg':msg})
    else:
        return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def categories(request):
    return render(request, 'categories.html')
