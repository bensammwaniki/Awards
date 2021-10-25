from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("profile/", views.profile),
    path('profile/update/', views.update_profile, name='update.profile'),
    path('add/', views.postimage, name='save.project'),
    path('display/<int:id>/', views.show_image, name='display.project'),
    path('display/rate/<int:id>/', views.rating, name='rate.project'),

]