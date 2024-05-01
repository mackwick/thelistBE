from django.db import models

# Create your models here.
class Show(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=20, default='tv show', blank=True)
    genre=models.CharField(max_length=20, blank=True)
    recby=models.CharField(max_length=30, blank=True)
    watched=models.BooleanField(default=False)    
    image=models.CharField(max_length=300, blank=True)
    user=models.CharField(max_length=200, blank=True)