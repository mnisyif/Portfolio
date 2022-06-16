from dbm.ndbm import library
from json import tool
from django.contrib import admin
from .models import Project, Summary, Experience, JobDescription, Education, Extracurricular, Language, Library, Software, Category

# Register your models here.
admin.site.register(Summary)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(JobDescription)
admin.site.register(Language)
admin.site.register(Library)
admin.site.register(Software)
admin.site.register(Education)
admin.site.register(Extracurricular)
admin.site.register(Category)