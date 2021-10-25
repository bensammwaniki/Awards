from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.
def home(request):
    projects = Post.objects.all().order_by('-posted_date')
    return render(request, 'index.html',{'projects': projects})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Post.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"projects": projects, "profile": profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':

        current_user = request.user

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        bio = request.POST['bio']

        profile_image = request.FILES['profile_pic']
        profile_image = cloudinary.uploader.upload(profile_image)
        profile_url = profile_image['url']

        user = User.objects.get(id=current_user.id)

        if Profile.objects.filter(user_id=current_user.id).exists():

            profile = Profile.objects.get(user_id=current_user.id)
            profile.profile_photo = profile_url
            profile.bio = bio
            profile.save()
        else:
            profile = Profile(user_id=current_user.id,
                              profile_photo=profile_url, bio=bio)
            profile.save_profile()

        user.first_name = first_name
        user.username = username
        user.last_name = last_name
        user.email = email

        user.save()

        return redirect('/profile', {'success': 'Updated your profile Successfully'})
    else:
        return render(request, 'profile.html', {'failed': 'Update Failed'})  



@login_required(login_url='/accounts/login/')
def postimage(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        project_url = request.POST['project_url']
        screenshort = request.FILES['screenshort']
        screenshort = cloudinary.uploader.upload(screenshort)
        screenshort_url = screenshort['url']
        project = Post(project_name=project_name, project_url=project_url, screenshort=screenshort_url,
                      profile_id=request.POST['user_id'], user_id=request.POST['user_id'])
        project.save_image()
        return redirect('/', {'success': 'Successfully posted'})
    else:
        return render(request, 'index.html', {'danger': 'posting Failed'})


@login_required(login_url='/accounts/login/')
def show_image(request, id):
    project = Post.objects.get(id=id)
    related_projects= Post.objects.filter(
                    user_id=project.user_id).order_by('-posted_date')
    return render(request, 'display.html', {'project': project, 'related_projects': related_projects,})


def rating(request, id):
    if request.method == "POST":

        project = Post.objects.get(id=id)
        current_user = request.user
        design_rate=request.POST["design"]
        usability_rate=request.POST["usability"]
        content_rate=request.POST["content"]

        Rating.objects.create(
            project=project,
            user=current_user,
            design_rate=design_rate,
            usability_rate=usability_rate,
            content_rate=content_rate,
            avg_rate=round((float(design_rate)+float(usability_rate)+float(content_rate))/3,2),
        )

        average_rating= (int(design_rate)+int(usability_rate)+int(content_rate))/3
        project.rate=average_rating
        project.update_project()

        return render(request, "display.html", {"success": "Rated Successfully", "project": project, "rating": Rating.objects.filter(project=project)})
    else:
        project = Post.objects.get(id=id)
        return render(request, "display.html", {"project": project})