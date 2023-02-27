from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Employer, Vacancy
from .forms import (
    EmployerRegistrationForm, ProfileForm, WorkExperienceForm, VacancyForm
)


def employer_registration(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            _ = Employer.objects.create(
                user=user,
                company_name=form.cleaned_data.get('company_name'),
                employee_count=form.cleaned_data.get('employee_count'),
                address=form.cleaned_data.get('address'),
                city=form.cleaned_data.get('city'),
                country=form.cleaned_data.get('country'),
                contact_info=form.cleaned_data.get('contact_info'),
                about=form.cleaned_data.get('about')
            )
            login(request, user)
            return redirect('home')
    else:
        form = EmployerRegistrationForm()


@login_required
def register_applicant(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        work_form = WorkExperienceForm(request.POST)
        if profile_form.is_valid() and work_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            work = work_form.save(commit=False)
            work.profile = profile
            work.save()

            messages.success(request, 'Profile created successfully')
            return redirect('home')
    else:
        profile_form = ProfileForm()
        work_form = WorkExperienceForm()

    context = {'profile_form': profile_form, 'work_form': work_form}
    return render(request, '....html', context)


@login_required
def add_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.author = request.user
            vacancy.save()
            return redirect('vacancies')
    else:
        form = VacancyForm()
    return render(request, '....html', {'form': form})


def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, '....html', {'vacancies': vacancies})


@login_required
def edit_vacancy(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id=vacancy_id)
    if request.user == vacancy.author:
        if request.method == 'POST':
            form = VacancyForm(request.POST, request.FILES, instance=vacancy)
            if form.is_valid():
                form.save()
                return redirect('vacancies')
