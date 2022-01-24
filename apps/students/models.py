from django.db import models

# Create your models here.

class Students(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    first_name = models.CharField(max_length=20, null= True)
    last_name = models.CharField(max_length=20, null=True)
    father_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    father_phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_enrollement = models.DateField()
    date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.first_name


