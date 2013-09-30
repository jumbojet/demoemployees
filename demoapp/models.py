from django.db import models


class Employee(models.Model):
    employeeid = models.IntegerField() # Employee Id
    name = models.CharField(max_length=1000) # Name of the Employee 
    dob = models.DateField() #  Date of birth of Employee
    salary = models.FloatField() #  Employee Salary
    ''' This is the function which Django uses to show the Employee Object
    - unicode represntation of employee'''
    def __unicode__(self):
        return unicode(self.employeeid)+"-"+unicode(self.name)
