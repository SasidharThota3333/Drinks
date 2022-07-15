from django.urls import path
from .views import *
urlpatterns = [
    path('', Login, name="Login"),
    path('registeration/', Registeration, name="Registeration"),
    path('contact/', Contact, name="Contact"),
    path('home/', Home, name="Home"),
    path('logout/', Logout, name="Logout"),
    path('adddrink/', AddDrink, name="AddDrink"),
    path('editdrink/<id>', EditDrink, name="EditDrink"),
    path('deletedrink/<id>', DeleteDrink, name="DeleteDrink"),
    path('climate/', Climate, name="Climate"),
    path('getToDo/', getToDo, name="getToDo"),
    path('deletetodo/<id>', DeleteTodo, name="Deletetodo"),
]
