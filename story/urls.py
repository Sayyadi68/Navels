from django.urls import path
from . import views

urlpatterns = [
    path('ReadStory/<str:storytitel>/<str:chaptername>', views.ReadStory , name='ReadStory'),
    path('WriteStory/',views.WriteStory, name='WriteStory'),

]

