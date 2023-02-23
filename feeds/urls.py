from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.FeedsView.as_view()),
    path("<str:username>", views.oneUserFeedsView.as_view()),
]
