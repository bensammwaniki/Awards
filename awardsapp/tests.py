from django.test import TestCase

from django.test import TestCase
from .models import *

# test image class


class PostTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
            first_name='bensam',
        )
        Post.objects.create(
            project_name='test_image',
            screenshort='https://doographics.com/assets/dg/images/cooking-youtube-thumbnail/cooking',
            project_url='test image url',
            profile_id=user.id,
            user_id=user.id
        )

    def test_image_name(self):
        image = Post.objects.get(image_name='test_image')
        self.assertEqual(image.image_name, 'test_image')


class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test_user',
            first_name='bensam',
            last_name='mwaniki'
        )
        Profile.objects.create(
            bio='test bio',
            profile_photo='https://doographics.com/assets/dg/images/cooking-youtube-thumbnail/cooking',
            user_id=user.id
        )

    def test_bio(self):
        profile = Profile.objects.get(bio='test bio')
        self.assertEqual(profile.bio, 'test bio')