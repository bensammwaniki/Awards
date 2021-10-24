from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.
def home(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Post.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"projects": projects, "profile": profile})
