# Generated by Django 5.0.2 on 2024-03-15 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_remove_subcategory_is_style'),
        ('users', '0014_alter_studentstats_is_enabled'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentstats',
            unique_together={('name', 'subcategory')},
        ),
    ]
