from django.shortcuts import render
import folium
import geocoder
from .models import GymCenter, Images, Contact, WorkDay
from django.core.paginator import Paginator

# Create your views here.


def all_gym(request):
    page = request.GET.get('page')
    p = Paginator(GymCenter.objects.all(), 9)
    gymAll = p.get_page(page)
    return render(request, 'allGymCenter.html', context={'gymAll':gymAll,})

def gym_center(request, id):
    gym = GymCenter.objects.get(id=id)
    gym_images = Images.objects.filter(gym_center_id=id)
    gym_contact = Contact.objects.filter(gym_center_id=id)
    gym_work_days = WorkDay.objects.filter(gym_center_id=id)
    address = gym.map_address
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[40.4 , 49.9], zoom_start=11)
    folium.Marker([lat,lng], tooltip='Click for more', popup=country).add_to(m)
    m = m._repr_html_()
    return render(request, 'gym_center_objects.html', context={'m':m , 'gym':gym,
    'gym_images':gym_images, 'gym_contact':gym_contact, 'gym_work_days':gym_work_days })

