from django.db import models

class User(models.Model):
    
    USER_TYPE_CHOICES = (   ##Include user type (staff/student)
        ("staff", "Staff"),
        ("student", "Student"),
    )
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username
