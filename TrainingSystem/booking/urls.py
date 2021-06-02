from django.urls import path
from . import views
from .views import courses, book, addCourse

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('course/<int:pk>', courses.as_view(), name='course'),
    path('book/course/<int:pk>', book.as_view(), name='book'),
    path('add/course', addCourse.as_view(), name='addCourse' )
]