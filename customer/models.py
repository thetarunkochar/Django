from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# models create database fields
# views converts model properties to templates

STATUS = (
    (0, 'Permanent'),
    (1, 'Temporary')
)


class Assignment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dob = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    reference = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name
