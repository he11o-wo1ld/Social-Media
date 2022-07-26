from distutils.command.upload import upload
import profile
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField()
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
