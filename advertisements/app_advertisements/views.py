from django.shortcuts import render
from .models import Advertisements
def index(request):
    advertisements = Advertisements.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request, 'index.html', context)
def top_sellers(request):
    return render(request, 'top-sellers.html')

