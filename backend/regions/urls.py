from django.urls import path
from . import views

urlpatterns = [
    path("", views.RegionsView.as_view()),
    path("<str:code>/", views.RegionDetailView.as_view()),
]   