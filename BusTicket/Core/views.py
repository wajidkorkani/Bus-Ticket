import geocoder
from django.shortcuts import render

# View to fetch and display the location
def home(request):
    g = geocoder.ip('me')  # Fetch location based on the current IP address
    latitude, longitude = g.latlng if g.latlng else (None, None)
    
    return render(request, 'index.html', {
        'latitude': latitude,
        'longitude': longitude
    })
