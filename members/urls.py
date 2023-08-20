from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('members/', views.members, name='members'),
    # path('members/sonira', views.sonira, name='members.sonira'),
    # path('members/fariha', views.fariha, name='members.fariha'),
    # path('members/freshta', views.freshta, name='members.freshta'),
    # path('members/maryam', views.maryam, name='members.maryam'),
    # path('members/khujesta', views.khujesta, name='members.khujesta'),
    # path('members/karima', views.karima, name='members.karima'),
    # path('members/mursal', views.mursal, name='members.mursal'),
    # path('members/nazanin', views.nazanin, name='members.nazanin'),
    # path('members/zahra', views.zahra, name='members.zahra'),
    # path('members/frohar', views.frohar, name='members.frohar'),
]