from django.shortcuts import render

from django.contrib.auth.views import (LoginView, )
from django.contrib.auth.views import PasswordResetView as PasswordResetView_
from django.conf import settings

def tmp_home(request):
    # return render(request, 'app_user/tmp_home.html', {})
    return render(request, 'base.html', {})



class PasswordResetView(PasswordResetView_):
    from_email = settings.EMAIL_FROM



