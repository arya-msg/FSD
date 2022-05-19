from django.db import models

# Create your models here.

class Degree(models.Model):
    title = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s'%(self.title, self.branch)

    def __eq__(self, other):
        return self.age == other.age

class Student(models.Model):
    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    dob = models.DateField('date of birth')
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s'%(self.roll_number, self.name, self.degree)
