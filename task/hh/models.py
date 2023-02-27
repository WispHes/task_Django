from django.db import models
from django.contrib.auth.models import User


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    employee_count = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=100)
    about = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    contacts = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.full_name


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    start_month = models.CharField(max_length=2)
    start_year = models.CharField(max_length=4)
    end_month = models.CharField(max_length=2)
    end_year = models.CharField(max_length=4)
    results = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Work experience'
        verbose_name_plural = 'Work experiences'

    def __str__(self):
        return self.company


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='vacancy_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
