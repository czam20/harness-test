from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    skills = models.ManyToManyField(Skill)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    