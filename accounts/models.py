from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class CustomUserManager(BaseUserManager):

    # For general User
    def create_user(self, phone_number, name, email, password=None):
        if not phone_number:
            raise ValueError(
                'User must enter an valid Phone Number: 8801711223344')
        name = name.title()
        email = email.lower()

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
# For SuperUser
    def create_superuser(self, phone_number, name, email, password=None):
        user = self.create_user(
            phone_number=phone_number,
            name=name,
            email=email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=150, verbose_name='name')
    email = models.EmailField(
        max_length=100, blank=True, null=True, verbose_name='email')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('name', 'email')

    objects = CustomUserManager()
    
# Return phone_number as a sting
    def __str__(self):
        return str(self.phone_number)

    def get_short_name(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lavel):
        return self.is_admin

    class Meta:
        verbose_name_plural = 'Users'
