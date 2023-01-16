from django.urls import path
from SampleApp import views
urlpatterns = [
    path('secondpage', views.secondpage,name='secondpage'),
    path('', views.FirstWeb,name="FirstWeb"),
]
