from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):

    def _create_user(self, name, last_name, email, is_admin, is_superuser, password):
        """Common method to create user"""
        if not name:
            raise ValueError('Users must have a name')

        if not last_name:
            raise ValueError('Users must have a last name')

        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            name=name,
            last_name=last_name,
            is_admin = is_admin,
            is_superuser = is_superuser,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, last_name, email, password):
        """Create a new normal user"""
        self._create_user(name, last_name, email, False, False, password)

    def create_superuser(self, name, last_name, email, password):
        """Create a new superuser"""
        self._create_user(name, last_name, email, True, True, password)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    history = HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='users/avatares', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user.email
