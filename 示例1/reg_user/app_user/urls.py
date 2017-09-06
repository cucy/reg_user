from django.conf.urls import url


from . import views

urlpatterns = [

    url(r'^$',views.tmp_home, name='tmp_home'),
    #url(r'^accounts/password/reset/$',views.PasswordResetView.as_view(), name='password_reset'),

]