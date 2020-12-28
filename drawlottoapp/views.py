import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from drawlottoapp.models import LottoNumber
from random import *


def draw_lotto(request):
    if request.method == "POST":
        temp = sample(range(1, 46), 6)
        new_temp = LottoNumber()
        new_temp.text = json.dumps(temp)
        new_temp.writer = request.user
        new_temp.save()

        return HttpResponseRedirect(reverse('drawlottoapp:draw_lotto'))
        # return render(request, 'drawlottoapp/list.html/', context={'temp_history_list': temp_history_list})

    else:
        return render(request, 'drawlottoapp/list.html/',
                      context={'temp_history_list': LottoNumber.objects.order_by('-id')},
                      )



