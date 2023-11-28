from PIL import Image
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    DEO = 1
    MANAGER = 2
    OWNER = 3
    ADMIN = 4
    SUPERUSER = 5
    ROLE_CHOICES = (
        (DEO, 'DEO'),
        (MANAGER, 'Manager'),
        (OWNER, 'Owner'),
        (ADMIN, 'Admin'),
        (SUPERUSER, 'Superuser'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_role_display()


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The Username field must be set'))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()
    objects = CustomUserManager()
    role = models.ManyToManyField(Role, verbose_name='Role')
    username = models.CharField(max_length=150, unique=True, verbose_name="User name",
                                help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
                                validators=[username_validator],
                                error_messages={
                                    "unique": "A user with that username already exists.",
                                }, )
    email = models.EmailField(unique=True, max_length=255, verbose_name='Email', error_messages={
        "unique": "A user with that email address already exists.",
    }, )
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    is_staff = models.BooleanField(default=False, null=False, verbose_name='Is Staff')
    is_admin = models.BooleanField(default=False, null=False, verbose_name='Is admin')
    is_superuser = models.BooleanField(default=False, null=False, verbose_name='Is supperuser')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    first_name = models.CharField(verbose_name="First name", max_length=150, blank=True)
    last_name = models.CharField(verbose_name="Last name", max_length=150, blank=True)
    date_joined = models.DateTimeField(verbose_name="Date joined", default=timezone.now)
    phone = models.CharField(max_length=25, blank=True)
    address = models.TextField(verbose_name="Address", blank=True, null=True)
    city = models.CharField(verbose_name="City", max_length=255, blank=True, null=True)
    country = models.CharField(verbose_name="Country", max_length=255, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        full_name = f"{self.first_name}  {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.username



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
