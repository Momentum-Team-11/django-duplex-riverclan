from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

# Create your models here.
