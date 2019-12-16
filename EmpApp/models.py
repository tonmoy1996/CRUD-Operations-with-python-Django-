from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# class UserProfile(models.Model):
#     user=models.OneToOneField(User)
#
#     def __str__(self):
#         return self.user.username



class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=30)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)

    class Meta:

        db_table="employee"


class Login(models.Model):

    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)

    class Meta:
        db_table="login"
