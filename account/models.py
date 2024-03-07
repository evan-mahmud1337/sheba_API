from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    crimesection_admin = models.BooleanField(default=False)
    entertainment_admin = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['crimesection_admin', 'entertainment_admin', 'phone']

    def __str__(self):
        return self.username
 

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null= True)
    first_name = models.CharField(max_length=50, blank=True, null= True)
    last_name = models.CharField(max_length=50, blank=True, null= True)
    social_media_link = models.CharField(max_length=400, blank=True, null= True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}'s profile"



@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name=instance.username)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=get_user_model())
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)