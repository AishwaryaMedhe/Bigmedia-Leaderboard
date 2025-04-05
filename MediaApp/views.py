from django.shortcuts import render
from .models import MediaOutlet
# Create your views here.

def leaderboard(request):
    outlets = MediaOutlet.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'outlets': outlets})

