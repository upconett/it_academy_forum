from django.db import models


class User(models.Model):
    username: str = models.CharField(max_length=20, unique=True)
    email: str = models.EmailField()
    password: str = models.CharField(max_length=35)

    def __str__(self):
        return self.username
