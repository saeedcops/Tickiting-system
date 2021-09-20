from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.conf import settings
import os
from . models import UserPreferences

# Create your views here.

# @login_required(login_url='/auth/login')
def index(request):
    exists=UserPreferences.objects.filter(user=request.user).exists()
    currency = []
    file_path = os.path.join(settings.BASE_DIR, 'currency.json')
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

        for k, v in data.items():
            currency.append({'name': k, 'value': v})

    context = {
        'currency': currency,
    }
    if exists:
        context['preferences'] = UserPreferences.objects.get(user=request.user)

    if request.method=='GET':

        return render(request,'preferences/index.html',context)

    else:
        currency=request.POST['currency']
        if exists:
            user_pref=UserPreferences.objects.get(user=request.user)
            user_pref.currency=currency
            context['preferences'] =user_pref
            user_pref.save()
        else:
            user_pref=UserPreferences.objects.create(user=request.user,currency=currency)
            context['preferences'] = user_pref
        messages.success(request,"Change Saved")

        return render(request,'preferences/index.html',context)