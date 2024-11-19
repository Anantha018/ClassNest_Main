# classnest_Base/models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

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
    created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)
    contact = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)  # GitHub field
    linkedin = models.URLField(blank=True)  # LinkedIn field
    
    def __str__(self):
        return f'{self.user.username} Profile'
