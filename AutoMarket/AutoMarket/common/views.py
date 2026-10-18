from django.apps import apps
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home_view(request: HttpRequest) -> HttpResponse:
    Vehicle = apps.get_model('vehicles', 'Vehicle')
    Manufacturer = apps.get_model("manufacturers", "Manufacturer")

    latest_vehicles = (Vehicle.objects.select_related('manufacturer').order_by('-created_at')[:6])

    vehicles_count = Vehicle.objects.count()
    manufacturers_count = Manufacturer.objects.count()

    context = {
        'latest_vehicles': latest_vehicles,
        'vehicles_count': vehicles_count,
        'manufacturers_count': manufacturers_count,
    }

    return render(request, 'common/home_view.html', context)

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'common/about_view.html')

def custom_404_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'common/custom_404_view.html', status=404)

def custom_500_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'common/custom_500_view.html', status=500)
