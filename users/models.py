from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users', primary_key=True, blank=True)
    first_name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    second_name = models.CharField(max_length=50, unique=True, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    joined_on = models.DateField(auto_now_add=True)

    class Meta:

        ordering = ['-joined_on']

    def __str__(self):

        return self.first_name