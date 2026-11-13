from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints: ClassVar[list[models.UniqueConstraint]] = [
            models.UniqueConstraint(fields=["user", "email"], name="unique_user_email")
        ]

    def __str__(self):
        return f"{self.name} - <{self.email}>"
