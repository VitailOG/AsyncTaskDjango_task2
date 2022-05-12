from django.urls import path

from main.api.views import MainApi, AudioApi, VideoApi

urlpatterns = [
    path('', MainApi.as_view()),
    path('audio/', AudioApi.as_view()),
    path('video/', VideoApi.as_view())
]
