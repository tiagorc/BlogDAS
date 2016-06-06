from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
