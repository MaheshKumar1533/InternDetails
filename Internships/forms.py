from django import forms
from .models import student, depts

ychoices =[
    ('1', 'I' ),
    ('2', 'II' ),
    ('3', 'III' ),
    ('4', 'IV' ),
]

dchoices =[]

for i in depts.objects.all():
    dchoices.append((i.dept, i.dept))

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = student
#         fields = ['name', 'rollno', 'year', 'dept']
#         widgets = {
#             'year': forms.Select(choices=ychoices),
#             'dept': forms.Select(choices=dchoices)
#         }
#     def __init__(self, *args, **kwargs):
#         super(StudentForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update({
#                 'id': "name",
#                 'name': "name",
#                 'placeholder': "Enter Student Name"
#             })
#         self.fields['rollno'].widget.attrs.update({
#                 'id': "rollNo",
#                 'name': "rollNo",
#                 'placeholder': "Enter Student Roll No"
#             })
#         self.fields['year'].widget.attrs.update({
#                 'id': "year",
#                 'name': "year",
#                 'placeholder': "Enter Student Year"
#             })
#         self.fields['dept'].widget.attrs.update({
#                 'id': "branch",
#                 'name': "branch",
#                 'placeholder': "Enter Student Year"
#             })

class BulkDataForm(forms.Form):
    file = forms.FileField()