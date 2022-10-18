from django.db import models



# Create your models here.
#Teacher models creatiojn
class Teacher(models.Model):
    Firstname = models.CharField(max_length=50)
    Lasttname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact=models.CharField(max_length=50)

    #This function converts the object into string for our comfortness
    def __str__(self) -> str:
        return self.Firstname

class Student(models.Model):
    Firstname = models.CharField(max_length=50)
    Lasttname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact=models.BigIntegerField()