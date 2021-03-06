from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

# image model 
class Post(models.Model):
    """
    This class takes care of the posted projects

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')

    screenshort = CloudinaryField('image')
    project_name = models.CharField(max_length=50)
    project_url = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    @classmethod
    def get_project_by_user(cls, user):
        project = cls.objects.filter(user=user)
        return project

    def save_image(self):
        self.save()

    def delete_project(self):
        self.delete()

    #  get by id
    @classmethod
    def get_one_project(cls, id):
        project = cls.objects.get(id=id)
        return project

    def update_project(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()    

    @classmethod
    def search_project(cls, search_term):
        project = cls.objects.filter(
                    project_name__icontains=search_term)
        return project    

    def __str__(self):
        return self.user.username       

    def __str__(self):
        return self.image_name




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_photo = CloudinaryField('image')

    bio = models.TextField(max_length=500, blank=True, null=True)

    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile       



class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    design = models.IntegerField(default=0)
    userbility = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    average_rate = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def update(self):
        self.save()

    def save_ratings(self):
        self.save()
        
    @classmethod
    def filter_by_id(cls, id):
        rating = Rating.objects.filter(id=id).first()
        return rating

    def __str__(self):
        return self.user.username
