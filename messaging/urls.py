from django.urls import path

from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.messages, name='messages'),
]
