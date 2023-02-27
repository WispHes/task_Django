from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, WorkExperience, Vacancy


class EmployerRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    employee_count = forms.IntegerField()
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    contact_info = forms.CharField(max_length=100)
    about = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = [
            'username', 'password1', 'password2', 'company_name',
            'employee_count', 'address', 'city', 'country', 'contact_info',
            'about'
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('full_name', 'about', 'contacts')


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = (
            'company', 'start_month', 'start_year',
            'end_month', 'end_year', 'results'
        )


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary', 'description', 'image']
