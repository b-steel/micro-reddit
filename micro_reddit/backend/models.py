from django.db import models
from .validators import validate_password

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length= 20, validators=[validate_password])

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    