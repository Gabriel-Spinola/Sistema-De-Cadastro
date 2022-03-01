from django.urls import path
from . import views # Import views from the current directory

# Define the views path 
urlpatterns = [
    path('<int:id>', views.index, name='index'), # If home go to views.index page
]

