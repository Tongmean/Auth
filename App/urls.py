from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name=''),
    path('LoginPage', views.LoginPage, name='Loginpage'),
    path('LogOutUser', views.LogOutUser, name='LogOutUser'),
    path('SignUpuser', views.SignUpuser, name='Signupuser'),
    path('SignUpadmin', views.SignUpadmin, name='Signupadmin'),
    path('Home', views.Home, name='Home'),
    path('Profile', views.MyProfile, name='Profile'),
    
    #ShipmentForm
    path('ShipmentRecordList', views.ShipmentRecondList, name='ShipmentRecordList'),
    path('InsertRecord', views.InsertRecord, name='InsertRecord'),
    path('MyActivities', views.MyActivities, name='MyActivities'),
    #ActionRecordList
    path('ActionRecordList', views.ActionRecordList, name='ActionRecordList'),
    path('AddAction<int:pk>', views.AddAction, name='Action'),
    path('ShipmentList', views.ShipmentList, name='ShipmentList'),
]
