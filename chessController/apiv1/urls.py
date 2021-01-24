
from django.urls import path
from .views import GameOpeningView

urlpatterns = [
    path('analysis', GameOpeningView.as_view()),
]
