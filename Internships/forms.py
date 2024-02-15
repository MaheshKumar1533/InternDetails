from django import forms
from .models import student, depts

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'rollno', 'year', 'dept']
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
        self.fields['year'].queryset = [1,2,3,4]
        self.fields['dept'].widget.attrs.update({
                'id': "studept",
                'class': "studeptyear"
            })
        self.fields['dept'].queryset = depts.objects.all()
        # self.fields['photo'].widget.arrts.update({
        #     'class': "file",
        #     'id': "file"
        # })
