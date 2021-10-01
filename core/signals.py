from django.db.models.signals import post_save
# from .models import User
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
import random
from .models import Profile
# from push_notifications.models import  GCMDevice
# and not instance.is_staff

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,name=instance.first_name,
                                email=instance.email,department="IT")
        print("\n User Created \n")
