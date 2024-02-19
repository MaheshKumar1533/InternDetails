from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import DeptUser, depts,student,internships
from .forms import StudentForm

# Create your views here.

User = 0

@login_required
def departments(request):
    return render(request, "departments.html")

def login(request, context={'authentication':0}):
    global User
    user = request.POST.get("username")
    password = request.POST.get("password")
    User =authenticate(username=user,password =password)
    if user==None or password==None:
        return render(request, "login.html")
    if User is not None:
        return render(request, "departments.html", context={'User':User, 'departments':depts.objects.all().values()})
    elif context['authentication']==0:
        return render(request, "login.html", context={'authentication':1})
    else:
        print("Failed")

def department(request):
    return render(request, "details.html")
def noAccess(request):
    return render(request,"noAccess.html")

def Details(request):
    global User
    Students = student.objects.filter(dept = User.dept)
    print(Students)
    return render(request,"details.html",context ={'User':User,'Students':Students,'internships':internships})

def create_student(request):
    global User
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form created")
            return render(request,'create_student.html',{"form":form})
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})
