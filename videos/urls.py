from django.urls import path
from .views import VideoListView, VideoDetailView

urlpatterns = [
    path('videos/', VideoListView.as_view()),
    path('videos/<str:id>/', VideoDetailView.as_view()),
]
