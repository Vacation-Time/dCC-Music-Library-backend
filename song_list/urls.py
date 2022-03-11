from django.urls import path
from . import views


urlpatterns = [  # creates website for this API
    path('', views.songs_list),
    path('<int:pk>/', views.song_detail),
]
