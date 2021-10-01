from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here. settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(
            User,
            related_name='userprofile',
            on_delete = models.CASCADE,null=True)
    # user = models.OneToOneField(User, on_delete= models.CASCADE)
    # domainuser = models.OneToOneField(User, on_delete= models.CASCADE,related_name='domainuser')
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    department=models.CharField(max_length = 50)
    # pc=models.ForeignKey(
    #         PC,
    #         on_delete = models.PROTECT,null=True)
    # branch=models.ForeignKey(
    #         Branch,
    #         on_delete = models.PROTECT,null=True)
    lastLogin = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-lastLogin']

class Ticket(models.Model):
    priority =  models.IntegerField(null=True)
    open_date = models.DateField(default=now)
    closed_date = models.DateField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    # user_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
            User,
            related_name='user',
            on_delete = models.CASCADE,null=True)
    admin = models.ForeignKey(
            User,
            related_name='admin',
            on_delete = models.CASCADE,null=True,blank=True)
    category = models.CharField(max_length=20, default="Support")

    def __str__(self):
        return self.category

    class Meta:
        ordering=['-open_date']


class Category(models.Model):
    name = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
