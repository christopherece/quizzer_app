# Generated by Django 4.2.11 on 2024-03-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_category_options_alter_option_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='photo_main',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
