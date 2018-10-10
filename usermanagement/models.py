from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=254)
    password = models.CharField(
        max_length=128)
    username = models.CharField(
        max_length=150,
        unique=True)
    first_name = models.CharField(
        max_length=40,
        help_text='User first name. (max 40 characters)')
    last_name = models.CharField(
        max_length=40,
        help_text='User last name. (max 40 characters)')
    is_admin = models.BooleanField(
        default=False,
        help_text="User who has admin permissions")
    phone = models.CharField(
        max_length=100,
        help_text='Phone number of user')
    city = models.CharField(
        max_length=100,
        help_text='City of user')
    jwt_secret_key = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)

    def update_user_secret_key(self):
        self.jwt_secret_key = uuid.uuid4()
        self.save()
