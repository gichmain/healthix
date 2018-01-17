from django import forms
from .models import Patient, Laboratory_Test


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'email', 'mobile', 'date_of_birth', 'id_number')


class LaboratoryTestForm(forms.Form):
    class Meta:
        model = Laboratory_Test
        fields = ('specimen', 'lab_test', 'duration', 'result', 'date_requested', 'lab', 'doctor', 'patient')
