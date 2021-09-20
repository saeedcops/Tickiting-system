from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.


class UserTicket(models.Model):
    priority =  models.CharField(max_length=20, default="Medium")
    open_date = models.DateField(default=now)
    closed_date = models.DateField(null=True)
    description = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name="user")
    # admin = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name="admin")
    category = models.CharField(max_length=20, default="Support")

    def __str__(self):
        return self.category

    class Meta:
        ordering=['-open_date']


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
