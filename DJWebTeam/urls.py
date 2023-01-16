from django.urls import path
from SampleApp import views
urlpatterns = [
    path('', views.FirstWeb,name="FirstWeb"),
]
