# Generated by Django 4.2 on 2023-06-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0012_alter_question_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
