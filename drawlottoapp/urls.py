from django.urls import path

from drawlottoapp.views import draw_lotto

app_name = "drawlottoapp"

urlpatterns = [
        path('draw_lotto/', draw_lotto, name="draw_lotto"),
    ]