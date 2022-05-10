from django.urls import path

from main.api.views import MainApi, AudioApi

urlpatterns = [
    path('', MainApi.as_view()),
    path('audio/', AudioApi.as_view())
]
