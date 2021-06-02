from django.urls import path
from . import views
from .views import courses

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('course/<int:pk>', courses.as_view(), name='course'),
]