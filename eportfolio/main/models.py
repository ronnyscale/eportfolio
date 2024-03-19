from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Achievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completion_date = models.DateField()
    location = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title