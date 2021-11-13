import geocoder

lat_log = [33.86465, -118.28533]
g = geocoder.osm([53.5343609, -113.5065084], method='reverse')
print(g) # Prints Edmonton
print(g.json['city']) # Prints Edmonton

g = geocoder.osm(lat_log, method='reverse')
print(g) # Prints Edmonton
print(g.json)

