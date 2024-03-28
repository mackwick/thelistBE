from django.db import models

# Create your models here.
class Show(models.Model):
    name=models.CharField(max_length=50)
    genre=models.CharField(max_length=20)
    recby=models.CharField(max_length=30)
    watched=models.BooleanField
    notes=models.TextField
    image=models.CharField(max_length=300)
    user=models.CharField(max_length=20)