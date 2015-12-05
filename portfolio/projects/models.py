import datetime

from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length = 50)
    pub_date = models.DateTimeField('date published')

    short_description = models.CharField(max_length = 200)
    long_description = models.TextField()
    mainimage = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return self.project_name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project)
    image = models.ImageField()
