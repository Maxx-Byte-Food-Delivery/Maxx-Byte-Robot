from django.db import models

class Staff(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    food_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'staff'

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    major = models.CharField(max_length=100)
    food_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'students'
