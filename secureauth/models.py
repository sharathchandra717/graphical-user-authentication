from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

fs = FileSystemStorage(location='secureauth/static/static_files')
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    myfile = models.FileField(storage=fs)
    identify_file = models.CharField(max_length=200, blank=True)
    status_file = models.CharField(max_length=10, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()