from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DeptUser, depts, student, internships
from django.contrib.auth import authenticate,login,logout
from .forms import BulkDataForm
import smtplib
from email.mime.text import MIMEText
import pandas as pd

User = None  #global user to handle the login through the dashboard
User = None  #global user to handle the login through the dashboard
#primary Dashboard without login
def primaryDashboard(request):
    return render(request,"primaryDashboard.html")

@login_required #login id mandatory to access the exclusive dashboard
def ExclusiveDashboard(request):
    global User
    # for internship in internships.objects.select_related('rollno').all():
    #     print(f"name:{internship.rollno.name}")
    internships_with_students = internships.objects.select_related('rollno').all()
    # for internship in internships_with_students:
    #     print(f"Internship ID: {internship.internId}, Student Name: {internship.rollno.name}, Roll Number: {internship.rollno.rollno}")
    print(internships_with_students.values())
    return render(request, "ExclusiveDashboard.html", {"User":User, 'departments':depts.objects.all().values(),'studentData':internships.objects.select_related('rollno').all()})

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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST["password"].encode("utf-8")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dept = request.POST.get("dept")
        # dept=request.POST.get("dept")
        # if not (username and password and email):
        #     print("error getting details!")
        #     return render(request, "facultyRegistrations.html")
        Newuser = {"username":username,"first_name":first_name,"last_name":last_name,"email":email,"dept":dept}
        Deptuser = DeptUser(**Newuser)
        print(first_name,last_name,dept)
        Deptuser.set_password(password)
        Deptuser.save()
        print("user saved successfully!")
        return redirect("custom_login",)
    return render(request,"facultyRegistrations.html")

@login_required
def create_student(request):
    global User
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = str(str(request.POST.get('rollNo')).upper())
        year = request.POST.get('year')
        branch = User.dept
        section = request.POST.get('section')
        newstudent = student(name=name, rollno=roll, year=year, dept=branch, section=section)
        newstudent.save()
        print("Student Created Successfully")
    return render(request, 'create_student.html', {"User": User})


#no aceess for wrong aurthorisation
def noAccess(request):
    return render(request, "noAccess.html")

@login_required
def Details(request):
    global User
    Students = student.objects.filter(dept=User.dept)
    # internships = internships.objects.filter(rollno=User.dept)
    common_primary_keys = Students.values_list('pk', flat=True)
    internship = internships.objects.filter(rollno__in=common_primary_keys)
    print(Students)
    print(internship)
    return render(request, "Details.html", context={'User': User, 'Students': Students, 'internship': internship})



def bulk_data_input(request):
    if request.method == 'POST':
        form = BulkDataForm(request.POST, request.FILES)
        if form.is_valid():
            df = pd.read_excel(request.FILES['file'])
            for index, row in df.iterrows():
                try:
                    user = student.objects.create(name=row['Name'], rollno=row['Roll Number'], year=row['Year'],section=row['Section'],dept=row['Department'])
                    user.save()
                    print("Saving >>>")
                except IntegrityError:
                    pass
            return redirect('custom_login')
    else:
        form = BulkDataForm()
    return render(request, 'bulk_update.html', {'form': form})


"""
example to store internships details using the student table:

--> 
from Interships.models import student,internships
# get a student instance
rollno = request.POST.get("rollno")
student = Student.objects.get(rollno=rollno)

# Create an internship instance and assign it to the student
internship = Internship.objects.create(student=student, internshipName='',intern_type="online/offline" sdate='2024-01-01', edate='2024-03-01',certificate="")

"""
@login_required
def addInternship(request):
    if request.method == "POST":
        rollno = request.POST.get("rollno")
        try:
            currentStudent = student.objects.get(rollno=rollno)
            internshipName = request.POST.get("internshipName")
            domain = request.POST.get("domain")
            projectName=request.POST.get("projectName")
            status=request.POST.get("status")
            sdate = request.POST.get("sdate")
            edate = request.POST.get("edate")
            intern_type = request.POST.get("intern_type")
            certificate = request.POST.get("certificate")
            newInternship = internships.objects.create(rollno=currentStudent, internshipName=internshipName, domain=domain, 
            projectName=projectName, status=status, intern_type=intern_type, sdate=sdate, edate=edate,certificate=certificate)
            print(newInternship)
            newInternship.save()
        except student.DoesNotExist:
            print("Student does not exist")
            return redirect("custom_login")
        return redirect("ExclusiveDashboard")
    return render(request,'intern_details.html',{"User":User})

import smtplib
from email.mime.text import MIMEText

def send_otp(email, otp):
    # Set up email server
    sender_email = "filloutsurvey2024@outlook.com"
    sender_password = "Reset1998"
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587
    recipient_email = email

    # Create message
    subject = "OTP for Verification"
    body = f"Your OTP for login into the Internship Dashboard is: {otp}"
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
        print("OTP sent successfully.")

# Example usage:
# send_otp("recipient@example.com", "123456")



from random import randint as ri
def AssignCode():
	otp = ri(1000,9999)
	return otp

# def verifyPassword(request,newPassword):
#     global ForgetUser
#     EmailOutlook = ForgetUser.email 
#     otp = AssignCode()
#     send_otp(EmailOutlook, otp)
#     UserOtp = request.POST.get("otp")
#     if otp==UserOtp:
#         ForgetUser.update(password=newPassword)
#         ForgetUser.save()
#         print("Password Changed")
#         return redirect("custom_login")


from django.http import HttpResponse
from django.contrib import messages

def forgotPassword(request):
    print("Loaded....")
    if request.method == 'POST':
        username = request.POST.get('username')
        print(f"{username} got")
        dept = request.POST.get('dept')
        print(f"{dept} got")
        request.session['username'] = username
        request.session['dept'] = dept
        print("saved")
        ForgetUser = DeptUser.objects.get(username=username,dept=dept)
        EmailOutlook = ForgetUser.email
        print(ForgetUser.email)
        otp = AssignCode()
        #send_otp(EmailOutlook, otp)
        request.session['otp']=otp
        print(f"{otp} saved & got")
        return redirect('otpPage')
    return render(request, 'confirmpassword.html')

def otpPage(request):
    if request.method == 'POST':
        userOtp = int(request.POST.get('userOtp'))
        print(f"{userOtp} got")
        password = request.POST.get('password')
        print(f"{password} got")
        username = request.session.get('username')
        dept = request.session.get('dept')
        otp=int(request.session.get('otp'))
        print(f"{username} {otp} {dept} retrived")
        ForgetUser = DeptUser.objects.get(username=username,dept=dept)
        if ForgetUser:
            print(f"{ForgetUser}")
        # print(f"{ForgetUser} is valid user")
        # if ForgetUser:
        #     verifyPassword(newPassword)
        if otp == userOtp:
            # Clear session data
            request.session.clear()
            ForgetUser.set_password(password)
            # Process login or whatever action you want
            # return HttpResponse(f"OTP verified successfully for {username} from {dept}!")
            return redirect("custom_login")
        else:
            # Display error message
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request, 'password.html')

# def forgotPassword(request):
#     if request.method=="POST":
#         # username= input("Enter your Username")
#         username = request.POST.get("username")
#         dept = request.POST.get("dept")
#         newPassword = request.POST.get("newPassword")

#         global ForgetUser
#         ForgetUser = DeptUser.objects.get(username=username,dept=dept)
#         print(f"{ForgetUser} is valid user")
#         if ForgetUser:
#             verifyPassword(newPassword)
#     return render(request, "confrimpassword.html")
