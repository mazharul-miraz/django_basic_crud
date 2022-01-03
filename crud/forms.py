from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=70)
    address = forms.CharField(max_length=50)
