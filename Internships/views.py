from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DeptUser, depts, student, internships
from django.contrib.auth import authenticate,login,logout
from .forms import BulkDataForm
import pandas as pd

User = None  #global user to handle the login through the dashboard
#primary Dashboard without login
def primaryDashboard(request):
    return render(request,"primaryDashboard.html")

@login_required #login id mandatory to access the exclusive dashboard
def ExclusiveDashboard(request):
    global User
    return render(request, "ExclusiveDashboard.html", {"User":User, 'departments':depts.objects.all().values()})

#Authentication
def custom_login(request, context={'authentication':0}):
    global User
    user = request.POST.get("username")
    password = request.POST.get("password")
    User =authenticate(request,username=user,password =password)
    #to not display failure method primarly if np details provided
    if user==None or password==None:
        return render(request, "custom_login.html")
    if User is not None:
        login(request,User)
        return redirect('ExclusiveDashboard')
        #return render(request, "departments.html", context={'User':User, 'departments':depts.objects.all().values()})
    elif context['authentication']==0:
        return render(request, "custom_login.html", context={'authentication':1})
    else:
        print("Failed")

#logout view
def custom_logout(request):
    logout(request)
    global User
    User = None
    return redirect("custom_login",)
def register_form(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    dept=request.POST.get("dept")
    if not (username and password and email):
        print("error getting details!")
        return render(request, "facultyRegistrations.html")
    Newuser = {"username":username,"password":password,"first_name":first_name,"last_name":last_name,"email":email,"dept":dept}
    Deptuser = DeptUser(**Newuser)
    print("user saved successfully!")
    return redirect("custom_login",)

def create_student(request):
    global User
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('rollNo')
        year = request.POST.get('year')
        branch = User.dept
        newstudent = student(name=name, rollno=roll, year=year, dept=branch)
        newstudent.save()
        print("Student Created Successfully")
    return render(request, 'create_student.html', {"User": User})




#student details dashboard
def department(request):
    return render(request, "Details.html")

#no aceess for wrong aurthorisation
def noAccess(request):
    return render(request, "noAccess.html")


def Details(request):
    global User
    Students = student.objects.filter(dept=User.dept)
    print(Students)
    return render(request, "Details.html", context={'User': User, 'Students': Students, 'internships': internships})



def bulk_data_input(request):
    if request.method == 'POST':
        form = BulkDataForm(request.POST, request.FILES)
        if form.is_valid():
            df = pd.read_excel(request.FILES['file'])
            for index, row in df.iterrows():
                try:
                    user = student.objects.create(name=row['Name'], rollno=row['Roll No'], year=row['year'], dept=row['dept'])
                except IntegrityError:
                    pass
            return render(request, 'custom_login.html')
    else:
        form = BulkDataForm()
    return render(request, 'bulk_update.html', {'form': form})

def addInternship(request):
    return render(request,'intern_details.html')



def send_otp(email, otp):
    # Set up email server
    sender_email = "filloutsurvey2024@outlook.com"
    sender_password = "Reset1998"
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587
    recipient_email = email

    # Create message
    subject = "Forgetten Password"
    body = f"Your otp for user verification is: {otp}"
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    # Connect to the server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        # Log in to the email account
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Registered code sent successfully.")


from random import randint as ri
def AssignCode():
	otp = ri(1000,9999)
	return otp

def forgotPassword(request):
    # username= input("Enter your Username")
    username = request.POST.get("username")
    dept = request.POST.get("dept")
    newPassword = request.POST.get("newPassword")
    ForgetUser = DeptUser.objects.get(username=username,dept=dept) 
    print(f"{ForgetUser} is valid user")
    if ForgetUser:
        EmailOutlook = ForgetUser.email 
        otp = AssignCode()
        send_otp(EmailOutlook, otp)
        UserOtp = request.POST.get("otp")
        if otp==UserOtp:
            ForgetUser.update(password=newPassword)
            return redirect("custom_login",)
    return render(request, "forgotPassword.html")
