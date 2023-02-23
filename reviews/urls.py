from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ReviewsView.as_view()),
]
