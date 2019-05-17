
from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER = (
        ('M', 'male'),
        ('F', 'female'),
        ('NONB', 'non-binary'),
        ('PNS', 'prefer not to say'),
)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0, blank=True)
    gender = models.CharField(
            max_length=30,
            choices=GENDER,
            )
    address = models.CharField(max_length=120, blank=True)
    position = models.CharField(max_length=50)
