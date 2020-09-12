from django.urls import path
from .views import *

app_name = "users"

urlpatterns=[
    path('<int:user_id>/follow_toggle/', follow_toggle, name="follow_toggle"),
    path('mypage/',mypage, name="mypage"),
]