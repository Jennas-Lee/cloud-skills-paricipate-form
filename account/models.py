from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, major_type, phone):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            major_type=major_type,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, name, major_type, phone):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            major_type=major_type,
            phone=phone
        )

        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True
    )
    name = models.TextField(max_length=5)
    major_type = models.IntegerField()
    phone = models.TextField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'major_type', 'phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class aws_account(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
