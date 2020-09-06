from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [


 path('state/', StateView.as_view(),name="state"),
path('requesttype/', RequestTypeView.as_view(),name="requesttype"),
path('status/', StatusView.as_view(),name="status"),
 path('newrequest/',NewRequestView.as_view(),name="newrequest"),
 path('updaterequest/<int:pk>',UpdateRequestView.as_view(),name ="updaterequest"),


]