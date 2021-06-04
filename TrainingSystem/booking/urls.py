from django.urls import path
from . import views
from .views import courses, book, addCourse, addProgram, viewCourse
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('course/<int:pk>/', courses.as_view(), name='course'),
    path('book/course/<int:pk>/', book.as_view(), name='book'),
     path('view/course/<int:pk>/', viewCourse.as_view(), name='viewCourse'),
    path('add/course/', addCourse.as_view(), name='addCourse' ),
    path('add/program/', addProgram.as_view(), name='addProgram'),
]