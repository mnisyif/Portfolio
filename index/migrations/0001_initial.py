# Generated by Django 4.0.4 on 2022-06-16 00:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=250)),
                ('study_time', models.CharField(max_length=25)),
                ('field', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=25)),
                ('team', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(default='some string', max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=20)),
                ('profession', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lib_name', models.CharField(max_length=20)),
                ('profession', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_name', models.CharField(max_length=20)),
                ('profession', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('per_des', models.CharField(max_length=200)),
                ('phone_num', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='media/projects/covers')),
                ('desc', models.CharField(max_length=512)),
                ('comp_date', models.DateTimeField(verbose_name='date completed')),
                ('project_url', models.CharField(default='SOME STRING', max_length=250)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.category')),
                ('langs', models.ManyToManyField(blank=True, to='index.language')),
                ('libs', models.ManyToManyField(blank=True, to='index.library')),
                ('soft', models.ManyToManyField(blank=True, to='index.software')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=25)),
                ('employer', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('job_desc', models.ManyToManyField(to='index.jobdescription')),
            ],
        ),
    ]
