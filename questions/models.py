from django.db import models

# Create your models here.
class Question(models.Model):
    CHOICES = [
        ('Addition','Addition'),
        ('Subtraction','Subtraction'),
        ('Multiplication','Multiplication'),
        ('Division','Division'),

    ]
    text = models.TextField()
    explanation = models.TextField(blank=True, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.CharField(max_length=50, choices=CHOICES, blank=True)


    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)



    def __str__(self):
        return self.text


