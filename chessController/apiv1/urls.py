
from django.urls import path
from .views import GameOpeningView
from .views import CreateGameOpeningView

urlpatterns = [
    path('analysis', GameOpeningView.as_view()),
    path('create-opening', CreateGameOpeningView.as_view()),
]
