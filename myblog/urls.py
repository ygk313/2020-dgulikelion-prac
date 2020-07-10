from django.contrib import admin
from django.urls import path, include
import introduction.urls
import posts.urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('introduction/', include('introduction.urls')),
    path('', views.main, name="main"),
    path('posts/', include('posts.urls')),
]
