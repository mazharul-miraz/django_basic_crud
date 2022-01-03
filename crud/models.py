from django.db import models
from django.db.models.fields import CharField, EmailField, IntegerField


# Create your models here.
class studentInfo(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField(max_length=70)
    address= models.CharField(max_length=70)

    # CHOICES = [('M','Male'),('F','Female')]
    # Gender=models.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
