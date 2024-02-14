from django import forms
from .models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'rollno', 'year', 'dept', 'photo']
