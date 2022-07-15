from django.shortcuts import render, redirect
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from sqlalchemy import null
from .models import *
from rest_framework.decorators import api_view
from .forms import *
# Create your views here.


# User Login
def Login(request):
    if request.method == "POST":
        username = request.POST["UserName"]
        password = request.POST["Password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            messages.success(
                request, ("There is an error loggin, Try again..."))
            return redirect("Login")
    else:
        return render(request, "Login.html")

# Create USER


def Registeration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        c = User.objects.create_user(
            username=username, email=email, password=password)
        c.save()
        messages.success(
            request, ("Congrats!... User Registered Successfully"))
        return redirect("Login")
    return render(request, "Registeration.html")

# Contact


def Contact(request):
    return render(request, "Contact.html")

# Landing or Home Page


@api_view(['GET'])
def Home(request):
    Drinks_obj = Drinks.objects.all()
    return render(request, "Home.html", {'dataframes': Drinks_obj})

# logout


def Logout(request):
    logout(request)
    return redirect("Login")

# Add Drink


def AddDrink(request):
    if request.method == "POST":
        form = Drinks_Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home")
    else:
        form = Drinks_Forms
        return render(request, "AddUser.html", {"form": form})

# Edit Drink


def EditDrink(request, id):
    Drinks_obj = Drinks.objects.get(pk=id)
    form = Drinks_Forms(request.POST or None, instance=Drinks_obj)
    if form.is_valid():
        form.save()
        return redirect("Home")
    else:
        return render(request, "EditUser.html", {'form': form})

# Delete Drink


def DeleteDrink(request, id):
    Drinks_obj = Drinks.objects.get(pk=id)
    Drinks_obj.delete()
    return redirect("Home")


# Climate
'''def Climate(request):
    target = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=51.48&lon=-3.18&exclude=hourly,daily&appid=88ba1f354e8be15b806186566a72ad24').json()
    return render(request,'Climate.html',{'target':target})'''


def Climate(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=88ba1f354e8be15b806186566a72ad24'
    city = 'UNITED KINGDOM'
    if request.method == "POST":
        city = request.POST['City'].upper()
    city_weather = requests.get(url.format(city)).json()

    if city_weather['cod'] == "404" or city_weather['cod'] == "400":
        messages.success(
                request, (city + " Not Found!! 'United Kingdoms' Weather is shown defaulty!!"))
        city = 'UNITED KINGDOM'
        city_weather = requests.get(url.format(city)).json()
    
    temp =float(str(city_weather['main']['temp'])[0:6])
    temincel ='{:.2f}'.format((temp -32) * (5/9))

    weather = {
        'city': city,
        'temperature':temincel,
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    context = {'weather': weather}
    return render(request, 'Climate.html', context)


def getToDo(request):
    ToDo_obj = ToDo.objects.all()
    form = ToDo_Forms
    if request.method == "POST":
        form = ToDo_Forms(request.POST)
        if form.is_valid():
            form.save()
    form = ToDo_Forms
    return render(request, "ToDo.html", {"form": form, 'dataframes': ToDo_obj})


def DeleteTodo(request, id):
    ToDo_obj = ToDo.objects.get(pk=id)
    ToDo_obj.delete()
    ToDo_obj = ToDo.objects.all()
    form = ToDo_Forms
    return redirect("getToDo")
