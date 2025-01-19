from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, first_name='', last_name='', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True) # Custom primary key
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) # Hashed password
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    join_date = models.DateTimeField(auto_now_add=True) # Timestamp of when the user was created
    last_login = models.DateTimeField(blank=True, null=True) # Timestamp of when the user last logged in

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_custom',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_custom',
        blank=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
    
# class User(AbstractUser):
#     email = models.EmailField(unique=True)

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='user_set_custom',
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='user_set_custom',
#         blank=True,
#     )

#     is_verified = models.BooleanField(default=False)

#     def __str__(self):
#         return self.username