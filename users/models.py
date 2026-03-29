from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="email", help_text="Enter your email")
    username = models.CharField(max_length=150, verbose_name="username", help_text="Enter your username", null=True,
                                blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username if self.username else self.email

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
