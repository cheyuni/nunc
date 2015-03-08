# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect

# Create your views here.
def profile(requests):
    user = requests.user
    if user.is_authenticated:
        profile = requests.POST.get('profile')
        user.profile = profile
        user.save()
        return redirect('/card')
