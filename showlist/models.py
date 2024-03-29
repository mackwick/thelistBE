from django.db import models

# Create your models here.
class Show(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=20, default='tv show')
    genre=models.CharField(max_length=20)
    recby=models.CharField(max_length=30, blank=True)
    watched=models.BooleanField(default=False)    
    image=models.CharField(max_length=300, blank=True)
    user=models.CharField(max_length=20, blank=True)