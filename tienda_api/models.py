from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('Usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo base de datos para usuarios en el sistema"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


class Client(models.Model):
    __tablename__ = "client"
    id = models.AutoField(primary_key=True)
    identification = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Store(models.Model):
    __tablename__ = "store"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    direction = models.CharField(max_length=100)


class Product(models.Model):
    __tablename__ = "product"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='stores')
