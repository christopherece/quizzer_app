from django.db import models
from django.contrib.auth.models import User

from pages.models import Category, Subcategory, Question, Option
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    UserType = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profiles/user-default.png', null=True, blank=True)
    user_type = models.CharField(max_length=200, choices=UserType, default='Student')
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)
    def __str__(self):
        return str(self.name)
    
class StudentStats(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING)
    subcategory = models.ForeignKey(Subcategory, blank=True, null=True, on_delete=models.DO_NOTHING)
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    score_percentage = models.FloatField(default=0)
    is_enabled = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)
    # class Meta:
    #     unique_together = ('name', 'subcategory')

    def __str__(self):
        return str(self.user)

