import json

from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.utils.datetime_safe import datetime

from drawlottoapp.models import LottoNumber

from random import *


def draw_lotto(request):
    if request.method == "POST":
        new_temp = LottoNumber()

        # temp = sample(range(1, 46), 6)
        # new_temp.game = sorted(temp)
        new_temp.writer = request.user

        # 살릴꺼 requestime = timezone.now()
        # 살릴꺼 new_temp.lottocount = requestime.isocalendar()[1] + 944

        # testx = request.user.id
        # testy = [{'writer_id': 4, 'name_count': 9}, {'writer_id': 6, 'name_count': 10}]

        # 살릴꺼 dbdata = LottoNumber.objects.values('writer_id').annotate(name_count=Count('writer_id')).filter(name_count__gt=1)
        # 윗줄설명 : db의 writer_id별로 숫자가 몇인지 뽑은 코드,, test2처럼 값이 나옴

        # 살릴꺼 i = 0
        # 살릴꺼 for i in range(len(dbdata)):
        # 살릴꺼     if request.user.id == dbdata[i]['writer_id']:
        # 살릴꺼         new_temp.charpoint = dbdata[i]['name_count']
        # 살릴꺼 i = i + 1
        # 윗줄설명 : test의 갯수(leg)를 범위(range)에서 i는 커지면서,, 유저 id가 몇번 인덱스 인지 if문으로 확인해주고, 인덱스 발견시, 갯수 출력!

        # x = LottoNumber.objects.filter(writer_id=request.user.id)
        # new_temp.test = x[1]['writer_id']

        new_temp.save()

        return HttpResponseRedirect(reverse('drawlottoapp:draw_lotto'))
        # return render(request, 'drawlottoapp/list.html/', context={'temp_history_list': temp_history_list})

    else:
        return render(request, 'drawlottoapp/list.html/',
                      context={'temp_history_list': LottoNumber.objects.order_by('-id')},
                      )



