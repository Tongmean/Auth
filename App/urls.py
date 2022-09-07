from django.urls import path
from . import views
urlpatterns = [
    # path('', views.Home, name=''),
    path('', views.LoginPage, name='Loginpage'),
    path('LogOutUser', views.LogOutUser, name='LogOutUser'),
    path('SignUpuser', views.SignUpuser, name='Signupuser'),
    path('SignUpadmin', views.SignUpadmin, name='Signupadmin'),
    path('Home', views.Home, name='Home'),
    path('Profile', views.MyProfile, name='Profile'),
    path('DiscrepancyRecord', views.DiscrepancyRecord, name='DiscrepancyRecord'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('Delete/<int:pk>', views.Delete, name='Delete'),
    
    path('HomePage', views.HomePage, name='HomePage'),
    path('GenCSV', views.GenCSV, name='GenCSV'),
    path('managemanagement', views.managemanagement, name='managemanagement'),
    path('DeleteUser/<int:pk>', views.DeleteUser, name='DeleteUser'),
    path('Genpdf/<int:pk>', views.Genpdf, name='Genpdf'),
    path('resetPass/<str:UserID>', views.resetPass, name='resetPass'),
    
    #ShipmentForm
    path('ShipmentRecordList', views.ShipmentRecondList, name='ShipmentRecordList'),
    path('InsertRecord', views.InsertRecord, name='InsertRecord'),
    path('Update/<int:pk>', views.Update, name='Update'),
    path('MyActivities', views.MyActivities, name='MyActivities'),
    #ActionRecordList
    path('ActionRecordList', views.ActionRecordList, name='ActionRecordList'),
    path('AddAction/<int:pk>', views.AddAction, name='Action'),
    path('ShipmentList', views.ShipmentList, name='ShipmentList'),
    path('MyTask', views.MyTask, name='MyTask'),
]
