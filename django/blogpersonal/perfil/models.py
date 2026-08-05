from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title