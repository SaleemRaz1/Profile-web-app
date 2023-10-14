from django.urls import path
from.import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('profile/',views.Profile,name="profile"),
    path('login/',views.Login,name="login"),
    path('register/',views.Register,name="register"),
    path('logout/',views.Logout,name="logout"),
    
]
