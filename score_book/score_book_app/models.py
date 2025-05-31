from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=20, null=False)
    Surname = models.CharField(max_length=20, null=False)
    Email = models.EmailField(max_length=60, null=False)
    Phone = models.CharField(max_length=16, null=False)

    @property
    def fio(self):
        return f'{self.Name} {self.Surname}'
    
    def __str__(self):
        return f'{self.fio} ({self.Email})'
    
    def __repr__(self):
        return f'Student(name="{self.Name}", name="{self.Surname}", name="{self.Email}")'

class Subject(models.Model):
    Name = models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.Name

    def __repr__(self):
        return f'Subject(name="{self.Name}")'

class Score(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Value = models.IntegerField(blank=False, null=False)
    Date = models.DateField(blank=False, null=False, auto_now_add=True)

    def __str__(self):
        return f'{self.Student.fio}: {self.Subject} -> {self.Value:.2f} ({self.Date})'

    def __repr__(self):
        return f'Student(student="{self.Student}", subject="{self.Subject}", value="{self.Value}")'