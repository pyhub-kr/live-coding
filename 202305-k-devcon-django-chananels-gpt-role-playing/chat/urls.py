from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.role_playing_room_detail, name="role_playing_room_detail"),
]
