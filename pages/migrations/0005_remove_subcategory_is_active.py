# Generated by Django 4.2.10 on 2024-03-10 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_subcategory_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='is_active',
        ),
    ]
