# Generated by Django 4.2.11 on 2024-03-13 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='Profile',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='Profile',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='Profile',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='Profile',
            new_name='profile',
        ),
    ]
