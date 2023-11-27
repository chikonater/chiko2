from django.db import models

# My models here.
class Person(models.Model):
    name = models.CharField( max_length=50)
    job = models.CharField( max_length=100)
    description = models.TextField( max_length=500)
    img = models.ImageField(blank=True)

    class Meta:
        verbose_name = ("Person")   

    def __str__(self):
        return self.name
    def get_name(self):
        self.name


class Services(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=500)
    img = models.ImageField(blank=True)
    class Meta:
        verbose_name = ("Services")
        

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    class Meta:
        verbose_name = ("Project")
        

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField(max_length=500)
    img = models.ImageField(blank=True)
    class Meta:
        verbose_name = ("Testimonial")
        
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=500)
    img = models.ImageField(blank=True)
    class Meta:
        verbose_name = ("Blog")
        
    def __str__(self):
        return self.title
   
