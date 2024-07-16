import pandas as pd
import folium
from folium.plugins import MarkerCluster, HeatMap
from datetime import datetime, timedelta

# Import Data
data = pd.read_csv('motorvehiclecollisions.csv', low_memory = False)

# Debug Preprocessing
print(data.head(10))
print(f'# of Rows {data.shape[0]}\n')

# Deletes Rows with Specified Empty Columns
data.dropna(subset = ['LATITUDE', 'LONGITUDE', 'NUMBER OF PERSONS KILLED', 'NUMBER OF PERSONS INJURED'], inplace = True)

# Cleaning Data
start_date = datetime.now() - timedelta(days=4*365)  # assuming a year has 365 days
data['CRASH DATE'] = pd.to_datetime(data['CRASH DATE']) # Converts Date from 9/11/2021 to 2021-9-11
data = data[data['CRASH DATE'] >= start_date] # Filters Dates to the Last 4 Years
data.sort_values(by = 'CRASH DATE', ascending = False, inplace = True)

# Debug Postprocessing
print(data.head(10))
print(f'# of Rows {data.shape[0]}')

# Map Visualization
map_nyc = folium.Map(location = [40.7128, -74.0060], tiles="Cartodb Positron", zoom_start = 12)

# Marking the Map
for index, row in data.head(20000).iterrows():
	color = 'red' if row['NUMBER OF PERSONS KILLED'] > 0 else 'orange' if row['NUMBER OF PERSONS INJURED'] > 0 and row['NUMBER OF PERSONS KILLED'] == 0 else 'blue'
	folium.CircleMarker(
		radius = 2,
		color = color,
		fill = True,
		fill_color = color,
		location = [row['LATITUDE'], row['LONGITUDE']],
		popup = f"{row['LATITUDE']}, {row['LONGITUDE']}<br>Fatalities: {int(row['NUMBER OF PERSONS KILLED'])}<br>Injured: {int(row['NUMBER OF PERSONS INJURED'])}"
	).add_to(map_nyc)

# Saving Marked Map
map_nyc.save('nyc_accidents_map.html')

# HeatMapping
heat_data = [[row['LATITUDE'], row['LONGITUDE']] for index, row in data.iterrows()]
HeatMap(heat_data, radius=12, blur=12, gradient={0.4: 'blue', 0.65: 'lime', 1: 'red'}, threshold=0.5).add_to(map_nyc)
map_nyc.save('nyc_accidents_heatmap.html')