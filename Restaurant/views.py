import imp
from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantCreate
from django.http import HttpResponse

# Create your views here.
def index(request):
    RestaurantList = Restaurant.objects.all()
    return render(request, 'Restaurant/listRestaurant.html', {'RestaurantList' : RestaurantList})

def addRestaurant(request):
    addRestaurant = RestaurantCreate()
    if request.method == 'POST':
        addRestaurant = RestaurantCreate(request.POST, request.FILES)
        if addRestaurant.is_valid():
            addRestaurant.save()
            return redirect('index')
        else:
            HttpResponse(""" Input Wrong. Please reload this website by click <a href="{{url:'index'}}">Reload</a>""")
    else:
        return render(request, 'Restaurant/editRestaurant.html', {'Restaurant_form':addRestaurant})

def editRestaurant(request, restaturant_id):
    restaturant_id = int(restaturant_id)
    try:
        restaturant_selected = Restaurant.objects.get(id = restaturant_id)
    except Restaurant.DoesNotExist:
        return redirect('index')
    restaturant_form = RestaurantCreate(request.POST or None, instance=restaturant_selected)
    if restaturant_form.is_valid():
        restaturant_form.save()
        return redirect('index')
    return render(request, 'Restaurant/editRestaurant.html', {'Restaurant_form':restaturant_form})

def deleteRestaurant(request, restaturant_id):
    try:
        restaturant_selected = Restaurant.objects.get(id = restaturant_id)
    except:
        return redirect('index')
    restaturant_selected.delete()
    return redirect('index')