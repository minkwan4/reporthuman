from django.contrib.auth.models import User
from django.db import models


class LottoNumber(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True, null=True)

    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='lotto', null=True)

