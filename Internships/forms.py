from django import forms

class BulkDataForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-input', 'id': 'fileInput'}))
