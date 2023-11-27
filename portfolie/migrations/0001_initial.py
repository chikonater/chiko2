# Generated by Django 4.2.6 on 2023-10-22 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='blog/% Y/% m/% d/')),
            ],
            options={
                'verbose_name': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='person/% Y/% m/% d/')),
            ],
            options={
                'verbose_name': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='project/% Y/% m/% d/')),
            ],
            options={
                'verbose_name': 'Project',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='service/% Y/% m/% d/')),
            ],
            options={
                'verbose_name': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='testimonial/% Y/% m/% d/')),
            ],
            options={
                'verbose_name': 'Testimonial',
            },
        ),
    ]
