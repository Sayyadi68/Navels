from django.urls import path
from account.views import Profile
from . import views

urlpatterns = [
    path('profile/Dashbord', views.Profile , name='profile'),
    path('logout/', views.auth_logout, name='logout'),
    path('login/', views.login_, name='login'),
    path('profile/connect', views.connect , name='connect'),
    path('profile/saves', views.saves , name='saves'),
    path('profile/setting', views.settings , name='setting'),
    path('profile/newstory', views.newstory , name='newstory'),
    path('verify_login/', views.verify_login, name='verify login'),
]

