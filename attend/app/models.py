from django.db import models

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    date=models.DateField()
    num=models.IntegerField()
    gender=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    pass1=models.CharField(max_length=30)

    def __str__(self):
        return self.name