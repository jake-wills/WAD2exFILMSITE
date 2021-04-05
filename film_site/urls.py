from django.urls import path
from film_site import views


app_name = 'film_site'

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('Account/', views.Account, name='Account'),
    path('logout/', views.user_logout, name='logout'),
    path('film/<slug:film_name_slug>/', views.show_film, name='show_film'),
    path('film/<slug:film_name_slug>/add_review/', views.add_review, name='add_review'),
    path('add_review/', views.add_review, name='add_review'),
    path('show_film_genre/<choice>/', views.show_film_genre, name="show_film_genre"),
    path('show_trending/', views.show_trending , name="show_trending"),
    path('contact_us/', views.contact_us , name="contact_us"),

]
