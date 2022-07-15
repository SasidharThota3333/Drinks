from pyexpat import model
from django.db import models

# Create your models here.

class Drinks(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=250)
    AvailableIN = models.CharField(max_length=250)
    Price = models.IntegerField()
    def __str__(self):
        return self.Name



CATEGORY_CHOICES = (
    ('Entertainment','Entertainment'),
    ('Food and Drink', 'Food and Drink'),
    ('Home','Home'),
    ('Life','Life'),
    ('Transport','Transport'),
    ('Utilities','Utilities'),
    ('General','General'),
)

class ToDo(models.Model):
    Description = models.CharField(max_length=250)
    Category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    Date = models.DateField()
    def __str__(self):
        return self.Description

