from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Drawlotto(models.Model):
    number = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
