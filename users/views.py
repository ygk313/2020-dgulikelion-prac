from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from posts.models import Post

@login_required
def follow_toggle(request, user_id):
    user = request.user
    followed_user = get_object_or_404(User, pk=user_id)

    is_follower = user in followed_user.followers.all()

    if is_follower:
        user.followings.remove(followed_user)
    else:
        user.followings.add(followed_user)
    return redirect('posts:main')

def mypage(request):
    user = request.user
    myprofile = get_object_or_404(User, pk = user.id)
    posts = Post.objects.filter(user=user)
    return render(request, 'users/mypage.html', {'myprofile':myprofile, 'posts':posts})