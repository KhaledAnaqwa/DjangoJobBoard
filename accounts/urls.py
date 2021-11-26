from django.urls import path,include
from . import views

app_name="accounts"
urlpatterns = [
    path('signup',views.SignUp,name="signup"),
    path('profile/',views.Profile,name="profile"),
    path('edit_profile',views.EditPorfile,name="edit_profile"),
]