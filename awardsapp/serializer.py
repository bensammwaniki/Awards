from rest_framework import serializers
from .models import Profile, Post


# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "profile_photo", "bio", "contact")

# Posts serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("user", "screenshort", "project_name", "project_url", "posted_date", "profile", "rate")