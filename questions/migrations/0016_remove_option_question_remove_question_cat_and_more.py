# Generated by Django 4.2.10 on 2024-02-29 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_category_question_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='cat',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
