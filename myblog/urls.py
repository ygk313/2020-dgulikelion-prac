from django.contrib import admin
from django.urls import path, include
import introduction.urls
import posts.urls, users.urls
from . import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('introduction/', include('introduction.urls')),
    path('', views.main, name="main"),
    path('posts/', include('posts.urls')),
   
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
