from django.contrib import admin

from .models import Employer, Profile, WorkExperience, Vacancy

admin.site.register(Employer)
admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(Vacancy)
