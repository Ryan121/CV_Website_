# Generated by Django 3.2.13 on 2022-06-08 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
    ]