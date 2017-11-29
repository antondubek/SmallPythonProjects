# Firstly Import The directories needed
import folium
import pandas

# Function which returns the color based on elevation input for Volcanoes
def get_marker_color(elevation):
    if elevation < 2000:
        return "green"
    elif elevation >= 2000 and elevation <= 3000:
        return "orange"
    else:
        return "red"

def get_citymarker_color(population):
    if population < 100000:
        return "green"
    elif population >= 100000 and population <= 300000:
        return "orange"
    else:
        return "red"

# Creates the basic map centered on Co-ordinates
# Note can add zoom_start = distInMiles, tiles = 'Mapbox Bright' or use help(folium.Map)
map = folium.Map(location = [55,-1.6])

"""
Pulls city data from a csv file. Check lines 42 & 43 for addition.
city_data = pandas.read_csv("worldcities.csv")

cities = list(city_data["city"])
city_latitudes = list(city_data["lat"])
city_longitudes = list(city_data["lng"])
city_population = list(city_data["pop"])
"""

# Creates a feature group called cities which adds two cities at the coordinates with popups and normal markers.
fg_Cities = folium.FeatureGroup(name = "Cities")
fg_Cities.add_child(folium.Marker(location=[54.978,-1.6178], popup=("Newcastle City Center"), icon = folium.Icon(color="green")))
fg_Cities.add_child(folium.Marker(location=[54.886,-1.4786], popup=("Sunderland"), icon = folium.Icon(color="red")))


#for city_lat, city_long, city_name, city_pop in zip(city_latitudes, city_longitudes, cities, city_population):
#    fg_Cities.add_child(folium.Marker(location=[city_lat,city_long], popup=str(city_name), icon = folium.Icon(color=get_citymarker_color(city_pop))))

# Reads the Volcanoes data from the volcano.txt file
data = pandas.read_csv("Volcanoes.txt")

# Creates three lists containing the latitudes, longitudes and elevation data from txt file.
latitudes = list(data["LAT"])
longitudes = list(data["LON"])
elevation = list(data["ELEV"])


'''
# Iterates through the lists and creates markers for each volcano with elevation popup!
# It also gets the color from the function defined at the top.

for lat, lon, elev in zip(latitudes, longitudes, elevation):
    fg.add_child(folium.Marker(location=[lat,lon], popup=("Elevation = " + str(elev)), icon = folium.Icon(color=get_marker_color(elev))))

# Could create a list with the longitudes and latitudes of stuff by hand if wanted but slow.

list = [[long,lat], [long,lat], [long,lat]]
for coordinates in list:
    fg.add_child(folium.Marker(location=coordinates, popup=("Newcastle City Center"), icon = folium.Icon(color="green")))
'''

# Creates the feature group volcanoes and adds markers from the longitude and latitude lists above,
# the color being taken from the function above.
fg_Volcanoes = folium.FeatureGroup(name='Volcanoes')
for lat, lon, elev in zip(latitudes,longitudes,elevation):
    fg_Volcanoes.add_child(folium.CircleMarker(location = [lat, lon], radius=6, fill_color = get_marker_color(elev), popup="Elevation = " + str(elev), color = 'grey', fill_opacity=0.7))

# Adds in the population feature group and adds the polygon data from the world.json file.
# Colours are decided using a lambda function which style_function must have.
fg_Population = folium.FeatureGroup(name='Population')
fg_Population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'), style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Adds the three function groups created above to the map
map.add_child(fg_Population)
map.add_child(fg_Cities)
map.add_child(fg_Volcanoes)


# Adds in layer control of the three feature groups, note must be after addition.
map.add_child(folium.LayerControl())

# Finally saves the map as an html file which can be opened within a browser.
map.save("NewcastleMap.html")
