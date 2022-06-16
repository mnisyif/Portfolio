import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Summary(models.Model):
    first_name = models.CharField(max_length = 50)
    #Murtadha
    last_name = models.CharField(max_length = 50)
    #Nisyif
    birth_date = models.DateField()
    #1997-05-23
    email = models.EmailField()
    #mnisyif@gmail.com
    per_des = models.CharField(max_length = 200)
    #I am an Electrical and Computer Engineering Student, who is self-driven to learn and deliver solutions. I am oriented towards, robots, automation and semi-conductors.
    phone_num = models.CharField(max_length = 15)
    #5195028463

    def __str__(self):
        return self.first_name + self.last_name

class Language(models.Model):
    lang_name = models.CharField(max_length = 20)
    profession = models.IntegerField(
        default = 0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.lang_name

class Library(models.Model):
    lib_name = models.CharField(max_length = 20)
    profession = models.IntegerField(
        default = 0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.lib_name

class Software(models.Model):
    soft_name = models.CharField(max_length = 20)
    profession = models.IntegerField(
        default = 0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.soft_name

class Category(models.Model):
    cat = models.CharField(max_length = 20)

    def __str__(self):
        return self.cat

class Project(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='media/projects/covers')
    desc = models.CharField(max_length = 512)
    comp_date = models.DateTimeField('date completed')
    project_url = models.URLField(default='SOME STRING')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    langs = models.ManyToManyField(Language, blank=True)
    libs = models.ManyToManyField(Library, blank=True)
    soft = models.ManyToManyField(Software, blank=True)
    

    def dateFinished(self):
        return self.comp_date.strftime('%B %Y')

    def __str__(self):
        return self.name

class JobDescription(models.Model):
    identifier = models.CharField(max_length = 50, default = 'some string')
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.identifier

class Experience(models.Model):
    position = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 25)
    employer = models.CharField(max_length = 100)
    location = models.CharField(max_length = 50)
    job_desc = models.ManyToManyField(JobDescription)

    def __str__(self):
        return self.position

class Education(models.Model):
    school_name = models.CharField(max_length = 250)
    #University of Guelph, Guelph, ON 
    study_time = models.CharField(max_length = 25)
    #2019-2023
    field = models.CharField(max_length = 50)
    # BACHELORS OF ENGINEERING IN COMPUTER ENGINEERING
    description = models.CharField(max_length = 250)

    def __str__(self):
        return self.school_name

class Extracurricular(models.Model):
    place = models.CharField(max_length = 100)
    position = models.CharField(max_length = 50)
    time = models.DateField()
    team = models.CharField(max_length = 100)

    def short_date(self):
        return self.time.strftime('%B %Y')

    def __str__(self):
        return self.place

