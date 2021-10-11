from django.db.models.signals import post_save
# from .models import User
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
import random
from .models import AdminProfile,UserProfile,PC,Branch
# from push_notifications.models import  GCMDevice
# and not instance.is_staff

@receiver(post_save, sender=User)
def post_save_create_profile(sender, update_fields,instance, created, **kwargs):
    
    if instance.first_name:
        # user=User.objects.get(instance)
        print("\n\n\n\n Created? \n",str(instance.is_staff))
        if instance.is_staff:
            try:
                AdminProfile.objects.get(user=instance)
                print("\n\n\n\n Admin Exist \n")
                
            except ObjectDoesNotExist:
                
                print("\n\n\n\n Admin Created \n")
                AdminProfile.objects.create(user=instance,branch=Branch.objects.get(pk=2),
                                            pc=PC.objects.get(pk=2),name=instance.username,
                                            email=instance.email,position="IT",phone="012232233")

        else:
            try:
                UserProfile.objects.get(user=instance)
                print("\n\n\n\n User Exist \n")
                
            except ObjectDoesNotExist:
                print("\n\n\n\n User Created \n")
                UserProfile.objects.create(user=instance,branch=Branch.objects.get(pk=2),
                                        pc=PC.objects.get(pk=2),name=instance.username,
                                        email=instance.email,department="HR")

        
