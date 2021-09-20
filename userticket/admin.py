from django.contrib import admin
from .models import UserTicket,Category
from userpreferences.models import UserPreferences

# Register your models here.

admin.site.register(UserTicket)
admin.site.register(Category)
admin.site.register(UserPreferences)
