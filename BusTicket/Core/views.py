import geocoder
from django.shortcuts import render

import requests

print(geocoder.ip("me"))

def get_address_from_ip(ip, api_key):
    url = f"http://api.ipstack.com/{ip}?access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Display the result
    print(f"IP: {ip}")
    print(f"Location: {data.get('city')}, {data.get('region_name')}, {data.get('country_name')}")
    print(f"IP Details: {data}")

# Example usage
api_key = "a33ecf357076eae694a591281e44cf1f"  # Replace with your actual ipstack API key
get_address_from_ip("39.39.85.15", api_key)  # Example IP address (Google DNS)


# View to fetch and display the location
def home(request):
    g = geocoder.ip('me')  # Fetch location based on the current IP address
    print(geocoder.ip("me"))
    latitude, longitude = g.latlng if g.latlng else (None, None)
    
    return render(request, 'index.html', {
        'latitude': latitude,
        'longitude': longitude
    })
