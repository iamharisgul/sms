from django.db import models

# Create your models here.

class Teachers(models.Model):
    first_name = models.CharField(max_length=20, null= True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number= models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    date = models.DateTimeField(auto_now=True)


    def __init__(self):
        return self.first_name



