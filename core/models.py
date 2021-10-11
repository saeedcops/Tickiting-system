from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here. settings.AUTH_USER_MODEL


class Branch(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'



class Server(models.Model):
    host_name = models.CharField(max_length=15)
    ip = models.CharField(max_length=15) 
    switch_port = models.IntegerField(default=0)
    vlan = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    cpu = models.CharField(max_length=10)
    hard_disk=models.CharField(max_length=10)
    os = models.CharField(max_length=10)
    mac = models.CharField(max_length=17) 
    model = models.CharField(max_length=20) 
    serial_num = models.CharField(max_length=17)
    role = models.CharField(max_length=30) 
    branch=models.ForeignKey(
            Branch,
            on_delete = models.PROTECT,null=True,blank=True)
    # category = models.CharField(max_length=20, default="Support")

    def __str__(self):
        return self.host_name

    class Meta:
        ordering=['-host_name']



class PC(models.Model):
    host_name = models.CharField(max_length=15)
    ip = models.CharField(max_length=15) 
    switch_port = models.IntegerField(default=0)
    vlan = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    cpu = models.CharField(max_length=10)
    hard_disk=models.CharField(max_length=10)
    os = models.CharField(max_length=10)
    mac = models.CharField(max_length=17) 
    model = models.CharField(max_length=20) 
    serial_num = models.CharField(max_length=17)     
    user = models.ForeignKey(
            User,
            related_name='userprofile',
            on_delete = models.PROTECT,null=True,blank=True)

    branch=models.ForeignKey(
            Branch,
            on_delete = models.PROTECT,null=True,blank=True)
    # category = models.CharField(max_length=20, default="Support")

    def __str__(self):
        return self.host_name

    class Meta:
        ordering=['-host_name']



class UserProfile(models.Model):
    user = models.OneToOneField(
            User,
            related_name='user',
            on_delete = models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 200)
    department=models.CharField(max_length = 10)
    pc=models.ForeignKey(
            PC,
            on_delete = models.PROTECT,null=True,blank=True)
    branch=models.ForeignKey(
            Branch,
            on_delete = models.PROTECT,null=True,blank=True)
#     last_login = models.DateTimeField(auto_now=True,null=True,blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-department']




class AdminProfile(models.Model):
    user = models.OneToOneField(
            User,
            related_name='admin',
            on_delete = models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    phone =models.CharField(max_length = 15)
    position =models.CharField(max_length = 20)
    pc=models.ForeignKey(
            PC,
            on_delete = models.PROTECT,null=True,blank=True)
    branch=models.ForeignKey(
            Branch,
            on_delete = models.PROTECT,null=True,blank=True)
#     last_login = models.DateTimeField(auto_now=True,null=True,blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']


class UserPermission(models.Model):
    apps = models.ManyToManyField(Category,null=True, blank=True)
    share=ArrayField(models.CharField(max_length=255,null=True),null=True,blank=True)
    user = models.OneToOneField(
            UserProfile,
            related_name='userpro',
            on_delete = models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.user.name



class Ticket(models.Model):
    priority =  models.IntegerField(null=True)
    open_date = models.DateField(default=now)
    closed_date = models.DateField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    user = models.ForeignKey(
            UserProfile,
            related_name='userticket',
            on_delete = models.CASCADE,null=True)
    admin = models.ForeignKey(
            AdminProfile,
            related_name='admin',
            on_delete = models.CASCADE,null=True,blank=True)
    pc=models.ForeignKey(
            PC,
            on_delete = models.PROTECT,null=True)
    branch=models.ForeignKey(
            Branch,
            on_delete = models.PROTECT,null=True)
    category = models.CharField(max_length=20, default="Support")

    def __str__(self):
        return self.user.name

    class Meta:
        ordering=['-open_date']
