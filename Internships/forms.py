from django import forms
from .models import student, depts

ychoices =[
    ('1', 'I' ),
    ('2', 'II' ),
    ('3', 'III' ),
    ('4', 'IV' ),
]

dchoices = []

for x in depts.objects.all():
    dchoices.append((x, x))




class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'rollno', 'year', 'dept', 'photo']
        widgets = {
            'year': forms.Select(choices=ychoices),
            'dept': forms.Select(choices=dchoices)
        }
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
                'id': "stuname",
                'class': "stuname",
                'placeholder': "Enter Student Name"
            })
        self.fields['rollno'].widget.attrs.update({
                'id': "sturoll",
                'class': "sturoll",
                'placeholder': "Enter Student Roll No"
            })
        self.fields['year'].widget.attrs.update({
                'id': "stuyear",
                'class': "studeptyear"
            })
        self.fields['dept'].widget.attrs.update({
                'id': "studept",
                'class': "studeptyear"
            })
        self.fields['photo'].widget.attrs.update({
            'class': "file",
            'id': "file"
        })
