from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from .views import *
from frontend.forms import UserLoginForm
urlpatterns = [
path('',views.LoginView.as_view(template_name="login.html",authentication_form=UserLoginForm),name='login'),
path("logout/",logout,name="logout"),
 path('login/', login,name="login"),
path("register/",register,name="register"),
    path("processregister",processregister,name="processregister"),
    path('newrequestform/',newrequestform,name="newrequestform"),
    path("processnewrequest/",processnewrequest,name="processnewrequest"),
    path("updaterequestform/",updaterequestform,name="updaterequestform"),
    path("processupdaterequest/<int:id>",processupdaterequest,name="processupdaterequest"),
   path("updaterequestsingle/<int:id>",updaterequestsingle,name="updaterequestsingle")
    ]