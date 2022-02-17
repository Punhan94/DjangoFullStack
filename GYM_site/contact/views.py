from .models import Contact, Ours_Contact
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
import folium
import geocoder
from django.contrib import messages

# Create your views here.

def contact_index(request):
    ours_contact = Ours_Contact.objects.all()
    for i in ours_contact:
        address = i.ours_coordinate
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[40.4 , 49.9], zoom_start=11)
    folium.Marker([lat,lng], tooltip='Click for more', popup=country).add_to(m)
    m = m._repr_html_()
    return render(request,'contact.html', context={'ours_contact':ours_contact,'m':m} )

def contact_elave(request):
    if request.method == 'POST':
        contact_first_name = request.POST.get('contact_first_name')
        contact_last_name = request.POST.get('contact_last_name')
        contact_subject = request.POST.get('contact_subject')
        contact_email = request.POST.get('contact_email')
        contact_detail = request.POST.get('contact_detail')
        new = Contact(contact_first_name=contact_first_name, contact_last_name=contact_last_name,
                         contact_email=contact_email, contact_detail=contact_detail,
                         contact_subject=contact_subject )
        new.save()
        messages.success(request, 'Mesajınız qəbul olundu')
    url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(url)