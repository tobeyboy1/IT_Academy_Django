from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=20, null=False)
    Surname = models.CharField(max_length=20, null=False)
    Email = models.EmailField(max_length=60, null=False)
    Phone = models.CharField(max_length=16, null=False)

class Subject(models.Model):
    Name = models.CharField(max_length=60, null=False)

class Score(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Value = models.IntegerField(blank=False, null=False)
    Date = models.DateField(auto_now=True)

