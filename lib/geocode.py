
#
# Get a coordinates from address
#
# Author -> vk.com/theagrik
#
# Catware, 2020
#

def Geocode(address):
    address = address.replace(" ", "+")
    json = Get("https://nominatim.openstreetmap.org/search?q="+ address + "&format=geojson")
    return json["features"][0]["geometry"]["coordinates"]