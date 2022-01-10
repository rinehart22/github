from django.db import models

# Create your models here.

#auth, User, UserCreationForm
#6 models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_no = models.IntegerField(blank = True, null=True) 
    images = models.ImageField(blank= True, null= True, upload_to= "images/")
    def __str__(self):
        return self.first_name

class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_no = models.IntegerField()

