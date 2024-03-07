# Generated by Django 4.2.10 on 2024-03-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], default='Student', max_length=200),
        ),
    ]
