from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('LoginPage', views.LoginPage, name='Loginpage'),
    path('LogOutUser', views.LogOutUser, name='LogOutUser'),
    path('SignUp', views.SignUp, name='Signup'),
    path('Home', views.Home, name='Home'),
    path('Profile', views.MyProfile, name='Profile'),
    

    #ShipmentForm
    path('ShipmentRecordList', views.ShipmentRecondList, name='ShipmentRecordList'),
    #ActionRecordList
    path('ActionRecordList', views.ActionRecordList, name='ActionRecordList'),
]
