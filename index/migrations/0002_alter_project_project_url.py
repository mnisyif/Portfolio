# Generated by Django 4.0.4 on 2022-06-16 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_url',
            field=models.URLField(default='SOME STRING'),
        ),
    ]
