Motor Vehicle Collision Data Visualization

Description
	This project visualizes motor vehicle collision data on an interactive map using Python's Folium library. The map displays markers at collision locations, each with a custom pop-up containing detailed information about the collision. This visualization helps identify collision hotspots and analyze trends in the data.

Features
	Interactive Map: Displays collision locations with markers.
	Custom Pop-ups: Each marker shows detailed information about the collision in a pop-up.
	Data Cleaning: Handles missing values and ensures data consistency.
	Customizable: Allows customization of pop-up appearance and content.

Installation
	Clone the repository:
		gh repo clone abdelrahmanebensahla/motorvehiclecollisions
		cd motorvehiclecollisions

	Install the required Python packages:
		pip install pandas folium

	Place your CSV file in the project directory and update the file path in the script:
		data = 'path_to_your_file.csv'  # Replace with your CSV file path

Usage
	Prepare your CSV file: Ensure your CSV file contains the following columns: date, latitude, longitude, and casualties.

	Run the script: Execute the Python script to generate the map.
		py mvcollisions.py

	Open the generated HTML file: The map will be saved as collisions_map.html in the project directory. Open this file in a web browser to view the map.

Customization
	Map Settings: Adjust the map's initial location and zoom level by modifying the location and zoom_start parameters.

License
	This project is licensed under the MIT License

Contributions are welcome! Please feel free to submit a Pull Request.

Acknowledgments
	Thanks to the developers of Folium and Pandas for their powerful libraries.
	Data provided by NYPD.