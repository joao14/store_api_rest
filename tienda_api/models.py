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
    """Model to create a new client"""
    __tablename__ = "client"
    id = models.AutoField(primary_key=True)
    identification = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date_creation = models.DateTimeField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['name']

    def __str__(self):
        return self.name

    def __str__(self):
        return self.lastname

    def __str__(self):
        return self.email


class Store(models.Model):
    """Model to create a new store"""
    __tablename__ = "store"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    direction = models.CharField(max_length=100)
    date_creation = models.DateTimeField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model the create a new product"""
    __tablename__ = "product"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    store_id = models.ManyToManyField(Store)
    date_creation = models.DateTimeField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name


class Album(models.Model):
    """Model to create a new album"""
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name


class Track(models.Model):
    """Track object about each albums"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering = ['title']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)

    def __str__(self):
        return '[ %d ]  %s' % (self.order, self.title)
