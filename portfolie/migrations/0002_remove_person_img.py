# Generated by Django 4.2.6 on 2023-10-22 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='img',
        ),
    ]
