from django.contrib.auth.models import User
from django.db import models


class LottoNumber(models.Model):

    text = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)

    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='lotto', null=True)

    lottocount = models.IntegerField(null=True)

    game = models.CharField(max_length=255, null=True)

    charpoint = models.IntegerField(null=True, default=1)
    charpoint_instance = models.IntegerField(null=True, default=2)

    test = models.CharField(max_length=255, null=True)

