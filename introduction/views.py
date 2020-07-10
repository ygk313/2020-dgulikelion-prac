from django.shortcuts import render

def profile(request):
    return render(request, 'introductions/profile.html')