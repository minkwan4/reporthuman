import json
import re

from bs4 import BeautifulSoup
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.utils.datetime_safe import datetime

from drawlottoapp.models import LottoNumber, ResultLotto
from selenium import webdriver

from random import *


def draw_lotto(request):

    if request.method == "POST":
        new_temp = LottoNumber()

        temp = sample(range(1, 46), 6)
        new_temp.game = sorted(temp)
        new_temp.writer = request.user

        requestime = timezone.now()
        new_temp.lottocount = requestime.isocalendar()[1] + 944

        dbdata = LottoNumber.objects.values('writer_id').annotate(name_count=Count('writer_id')).filter(name_count__gt=0)
        # 윗줄설명 : db의 writer_id별로 숫자가 몇인지 뽑은 코드,,

        i = 0
        for i in range(len(dbdata)):
            if request.user.id == dbdata[i]['writer_id']:
                new_temp.charpoint = dbdata[i]['name_count'] + 1
        i = i + 1
        # 윗줄설명 : test의 갯수(len)를 범위(range)에서 i는 커지면서,, 유저 id가 몇번 인덱스 인지 if문으로 확인해주고, 인덱스 발견시, 갯수 출력!

        # new_temp2 = ResultLotto.objects.values()
        # # 윗줄설명 : 로또번호 결과 나오값 admin에 입력해주면, 결과값들을 new_temp2에 저장
        #
        # if len(new_temp2)>0:
        #     new_temp.test = []
        #
        #     new_temp.test2 = []
        #     new_temp.test2.append(new_temp2[0]['lottocountresult'])
        #
        #     new_temp.test3 = []
        #     new_temp.test3.append(new_temp2[0]['result1'])
        #     new_temp.test3.append(new_temp2[0]['result2'])
        #     new_temp.test3.append(new_temp2[0]['result3'])
        #     new_temp.test3.append(new_temp2[0]['result4'])
        #     new_temp.test3.append(new_temp2[0]['result5'])
        #     new_temp.test3.append(new_temp2[0]['result6'])
        #
        #     new_temp.test4 = []
        #     new_temp.test4.append(new_temp2[0]['result7'])
        #
        #     if new_temp.lottocount == new_temp.test2[0]:
        #         j = 0
        #         for j in range(6):
        #             if new_temp.game[j] in new_temp.test3:
        #                 new_temp.test.append(new_temp.game[j])
        #         j = j + 1
        #
        #         if len(new_temp.test) == 6:
        #             new_temp.test.append("1등 입니다!")
        #         if len(new_temp.test) == 5:
        #             if new_temp.test4[0] in new_temp.game:
        #                 new_temp.test.append(new_temp.test4[0])
        #                 new_temp.test.append("2등 입니다!")
        #             else:
        #                 new_temp.test.append("3등 입니다!")
        #         if len(new_temp.test) == 4:
        #             new_temp.test.append("4등 입니다!")
        #         if len(new_temp.test) == 3:
        #             new_temp.test.append("5등 입니다!")
        #         if len(new_temp.test) < 3:
        #             new_temp.test.append("꽝 입니다!")
        #     else:
        #         new_temp.test.append("아직 결과가 나오지 않았습니다.")

        new_temp.save()

        return HttpResponseRedirect(reverse('drawlottoapp:draw_lotto'))
        # return render(request, 'drawlottoapp/list.html/', context={'temp_history_list': temp_history_list})

    else:
        return render(request, 'drawlottoapp/list.html/',
                      context={'temp_history_list': LottoNumber.objects.order_by('-id')},
                      )



