from django.urls import path

from .views import StateMatch, UpdateState

urlpatterns = [
    path('', StateMatch.as_view()),
    path('state/', StateMatch.as_view()),
    path('state/<int:pk>', UpdateState.as_view())
    ]