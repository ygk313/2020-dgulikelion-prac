from django.urls import path
from . import views

app_name ="posts"
urlpatterns =[
    path('', views.main, name="main"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('show/<int:id>/', views.show, name="show"),
]