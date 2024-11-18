# classnest_Base/models.py
from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is created

    def __str__(self):
        return self.title


class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    bio = models.TextField(max_length=500, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    links = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"