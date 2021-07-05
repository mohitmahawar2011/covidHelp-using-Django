from django.contrib import admin
from django.urls import path
from .views import homepage, HospitalDetailView
urlpatterns = [
    path('', homepage, name ='homepage'),
    path('hospital/<int:pk>', HospitalDetailView.as_view(),name='hospital_detail'),


]