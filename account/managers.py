from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, crimesection_admin, entertainment_admin, phone, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')

        user = self.model(
            username=username,
            crimesection_admin=crimesection_admin,
            entertainment_admin=entertainment_admin,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, crimesection_admin, entertainment_admin, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, crimesection_admin, entertainment_admin, phone, password, **extra_fields)
