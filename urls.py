
from django.urls import path
from . import views

urlpatterns = [

    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('farmerhome/',views.farmerhome,name='farmerhome'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('applyscheme/',views.applyscheme,name='applyscheme'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('createscheme/',views.createscheme,name='createscheme'),
    path('viewscheme/',views.viewscheme,name='viewscheme'),
    path('addcrops/',views.addcrops,name='addcrops'),
    path('viewcrops/',views.viewcrops,name='viewcrops'),
    path('cropdetails/',views.cropdetails,name='cropdetails'),
    path('apply/',views.apply,name='apply'),
    path('userdetails/',views.userdetails,name='userdetails'),
    path('applicationview/',views.applicationlist,name='applicationview'),
    path('viewappl/',views.viewApplication,name='viewappl'),
    path('myapplication/',views.myapplication,name='myapplication'),
    path('edit_crop/<int:crop_id>/', views.edit_crop, name='edit_crop'),
    path('delete_crop/<int:crop_id>/', views.delete_crop, name='delete_crop'),
    path('edit_scheme/<int:scheme_id>/', views.edit_scheme, name='edit_scheme'),
    path('delete_scheme/<int:scheme_id>/', views.delete_scheme, name='delete_scheme'),
   


]

