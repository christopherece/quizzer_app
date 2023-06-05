# Generated by Django 4.2 on 2023-06-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(blank=True, choices=[('Addition', 'Addition'), ('Subtraction', 'Subtraction'), ('Multiplication', 'Multiplication'), ('Division', 'Division')], max_length=50),
        ),
    ]
