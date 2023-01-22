from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=255)


class Class(models.Model):
    AM = 'AM'
    PM = 'PM'
    AVAILABLE_TIME_CHOICES = [
        (AM, 'morning (8-2)'), (PM, 'afternoon(2-8)')
    ]

    ONLINE = 'on'
    HYBRID = 'hy'
    ON_SITE = 'site'
    LOCATION_CHOICES = [
        (ONLINE, 'online'), (HYBRID, 'hybrid'), (ON_SITE, 'on-site')
    ]

    class_name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=255)
    available_time = models.CharField(
        max_length=10, choices=AVAILABLE_TIME_CHOICES)
    location = models.CharField(
        max_length=10, choices=LOCATION_CHOICES, default=ON_SITE)
    price = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_name
