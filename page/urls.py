from django.urls import path

from page.views import Home,chapters,UserInfo

urlpatterns = [
    path('', Home, name='index'),
    path('chapters/<str:storytitel>', chapters, name='chapters'),
    path('UserInfo/<str:userinfo>/storys', UserInfo , name='UserInfo')
]

