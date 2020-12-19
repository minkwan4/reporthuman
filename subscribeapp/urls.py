from django.urls import path

from subscribeapp.views import SubscriptionView, subscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', subscriptionListView.as_view(), name='list'),
]

