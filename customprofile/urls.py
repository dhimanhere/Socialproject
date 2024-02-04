from django.urls import path
from customprofile import views

urlpatterns = [
	path("", views.profile, name = "profile"),
	path('register/', views.register, name = "register"),
	path('login/', views.loginv,name = "login-c"),
	path('logout/', views.logoutv, name = "logout-c"),
]