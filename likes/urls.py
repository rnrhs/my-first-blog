from django.urls import path
from . import views

urlpatterns = [
    path('<int:user>/', views.add_like, name='add_like'),
    path('', views.get_liked, name='get_liked'),
    path('<int:user>/', views.dislike, name='dislike'),
]