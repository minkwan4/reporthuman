from django.contrib import admin

# Register your models here.
from drawlottoapp.models import LottoNumber, ResultLotto

admin.site.register(LottoNumber)
admin.site.register(ResultLotto)