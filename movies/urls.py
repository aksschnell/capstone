from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("movie/<int:id>", views.movie, name="movie"),
    path("profile/<int:id>", views.profile, name="profile"),

  
    #API
    path("api/movie/<int:id>", views.api_movie, name="api_movie"),
    path("api/review", views.review, name="review"),
    path("api/reaction", views.reaction, name="reaction"),
    
 
]