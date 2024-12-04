import folium
from folium import plugins

# Data: Cities with their coordinates (latitude, longitude) in West Java
city_coordinates = {
    'Bandung': (-6.9175, 107.6191),
    'Bogor': (-6.5951, 106.7891),
    'Cirebon': (-6.7002, 108.5507),
    'Sumedang': (-6.8581, 107.9279),
    'Depok': (-6.3916, 106.8265),
    'Bekasi': (-6.2347,3 106.9895),
    'Indramayu': (-6.483, 108.3060)
}

# Connections between cities in West Java (as edges)
province_connections = {
    'Bandung': ['Bogor', 'Cirebon', 'Sumedang'],
    'Bogor': ['Bandung', 'Depok', 'Bekasi'],
    'Cirebon': ['Bandung', 'Indramayu'],
    'Sumedang': ['Bandung'],
    'Depok': ['Bogor', 'Bekasi'],
    'Bekasi': ['Bogor', 'Depok'],
    'Indramayu': ['Cirebon']
}

# Function to visualize the map of cities in a province
def visualize_province_map(province_name):
    # Create a map centered around West Java (example coordinates: Bandung)
    map_center = city_coordinates['Bandung']
    m = folium.Map(location=map_center, zoom_start=10, control_scale=True)

    # Add markers for cities
    for city, (lat, lon) in city_coordinates.items():
        folium.Marker(
            location=[lat, lon],
            popup=city,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    # Add lines (edges) between connected cities
    for city, connected_cities in province_connections.items():
        city_lat, city_lon = city_coordinates[city]
        for connected_city in connected_cities:
            connected_lat, connected_lon = city_coordinates[connected_city]
            folium.PolyLine(
                locations=[(city_lat, city_lon), (connected_lat, connected_lon)],
                color='red',
                weight=2.5,
                opacity=1
            ).add_to(m)

    # Show the map
    m.save(f"{province_name}_map.html")
    print(f"Map saved as {province_name}_map.html")

# Input: Get the province name from the user
province_name = input("Enter the province name (e.g., 'West Java'): ")

# Visualize the map for the selected province
visualize_province_map(province_name)
