from django.db import models

# Create your models here.

#created database named as Register which will store 
#registration form data
class Register(models.Model):
    name=models.CharField(max_length=70)
    mobileno=models.IntegerField()
    address=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    state=models.CharField(max_length=70)

#created database named as Loan which will store
#loan form data
class Loan(models.Model):
    loanamt=models.IntegerField()
    duration_of_loan=models.IntegerField()
    ROI=models.IntegerField()


