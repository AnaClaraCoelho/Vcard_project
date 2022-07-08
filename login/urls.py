from django.urls import path
from . import views

urlpatterns = {
    path('login/',views.user_register),
    path('profile/',views.profile),
}
