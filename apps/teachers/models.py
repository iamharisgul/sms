from django.db import models
from apps.management.models import School, Class
from apps.management.models import User

# Create your models here.


class Teachers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20, null= True)
    last_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number= models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    date = models.DateTimeField(auto_now=True)
    classes = models.ManyToManyField(Class, related_name='Classes')

    def __str__(self):
        return self.first_name



