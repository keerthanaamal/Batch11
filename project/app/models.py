from django.db import models

# Create your models here.
from django. contrib. auth.models import AbstractUser

class User(AbstractUser):
    usertype = models.CharField(max_length=50)