from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png', null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)
    def __str__(self):
        return str(self.name)

