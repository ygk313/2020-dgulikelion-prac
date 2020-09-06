from django.urls import path
from .views import * 

app_name ="posts"
urlpatterns =[
    path('', main, name="main"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('show/<int:id>/', show, name="show"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
    path('<int:post_id>/post_like', post_like, name="post_like"),
    path('like_list/', like_list, name="like_list"),
]