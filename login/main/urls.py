from django.urls import path
from . import views # Import views from the current directory

# Define the views path 
urlpatterns = [
    path('', views.index, name='index'), # If home go to views.index page
    path('v1/', views.v1, name='view 1') # If home go to views.index page
]

