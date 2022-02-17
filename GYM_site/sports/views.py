from django.shortcuts import redirect, render
from .models import Sport, VideoSport

# Create your views here.

def sports_index(request):
    return render(request, 'sports.html')

def sport_detail(request,slug):
    sportSlug = Sport.objects.filter(slug=slug)
    if sportSlug:
        sport = Sport.objects.get(slug=slug)
        sportVideo = VideoSport.objects.filter(sport=sport)
        return render(request, 'sport_detail.html', context={'sport':sport, 'sportVideo':sportVideo})
    else:
        return redirect('sports_index')

def sports(request,id):
    sport = Sport.objects.get(id=id)
    sportVideo = VideoSport.objects.filter(sport=sport)
    return render(request, 'sport_detail.html', context={'sport':sport, 'sportVideo':sportVideo})
