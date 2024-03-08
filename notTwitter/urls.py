from django.urls import path

from . import views

app_name = 'notTwitter'

urlpatterns = [
    path('', views.index, name="index"),
    path('make-post/', views.make_post, name="make_post"),
]
