from django.shortcuts import render

# Create your views here.
def departments(request):
    return render(request, "Departments.html")