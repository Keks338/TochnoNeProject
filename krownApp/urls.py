from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('movies/top/', views.topMovies, name='topMovies'),
    path('movies/all/', views.allMovies, name='allMovies'),
    path('movies/all/filter/<slug:slug>', views.allMovies, name='filterMovies'),
    path('movies/detail/<int:pk>/', views.movieDetail, name='movieDetail'),
    path('auth/login/', views.loginPage, name='loginPage'),
    path('auth/signup/', views.signUp, name='SignUpPage'),
    path('auth/logout/', views.logoutUser, name='logoutUser'),
]