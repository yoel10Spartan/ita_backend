from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
 
class UserManager(BaseUserManager):
    def _create_user(self, name, last_name, password, email, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, last_name, password, email, is_staff=False, is_superuser=False, **extra_fields):
        return self._create_user(name, last_name, password, email, False, False, **extra_fields)

    def create_superuser(self, name, last_name, password, email, is_staff=True, is_superuser=True, **extra_fields):
        return self._create_user(name, last_name, password, email, True, True, **extra_fields)
 
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
 
    objects = UserManager()
    
    def get_full_name(self):
        return '{} {}'.format(self.name, self.last_name)
    
    class Meta:
        db_table = 'auth_user'
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']