from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def departments(request):
    return render(request, "Departments.html")

<<<<<<< HEAD
def login(request, context={'authentication':0}):
=======

def login(request,context={'authentication':0}):
>>>>>>> 1bec60682f16be1509e1e6fa98c6607c5d6416c5
    user = request.POST.get("username")
    password = request.POST.get("password")
    User =authenticate(username=user,password =password)
    if user==None or password==None:
        return render(request, "login.html")
    if User is not None:
        return render(request, "departments.html", context={'User':User})
    elif context['authentication']==0:
        return render(request, "login.html", context={'authentication':1})
    else:
        print("Failed")

<<<<<<< HEAD
def department(request):
    return render(request, "Details.html")
=======
def noAccess(request):
    return render(request,"noAccess.html")
>>>>>>> 1bec60682f16be1509e1e6fa98c6607c5d6416c5
