# import useful libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load growLocationsDataFrame from CSV
growLocationsDataFrame = pd.read_csv('GrowLocations.csv')

# Rename longitude and latitude columns in the original dataset for accurate plotting
growLocationsDataFrame = growLocationsDataFrame.rename(
    columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'})

# List of latitude and longitude pairs which will be used to plot location
#syntax -> [[long1,lat1],...]
# this is expressed as long, lat due to the bounding box dimensions instead of lat, long
points = []
for index, row in growLocationsDataFrame.iterrows():
    points.append([row['Longitude'], row['Latitude']]) 
#read image using pyplot. Scatter plot will be overlayed with this image
backgroundImageUK = plt.imread('map7.png')

# Create a scatter plot
generatedFigure, generatedAxes = plt.subplots(figsize=(10, 10))

# imshow method to display the map of UK as the background on the generatedAxes
#extent is used to specify the extent of the image. This will be used concurrently with xlim and ylim of the scatter plot.
#alpha is used to determine image transparency, adjusted for clearer view of towns (0 - max transparency).
generatedAxes.imshow(
    backgroundImageUK, extent=[-10.592, 1.6848, 50.681, 57.985], alpha=0.62)

# Plot each sensor location as a dot
longitude, latitude = np.transpose(points) # creates individual coordinate lists from points via numpy transpose
generatedAxes.scatter(longitude, latitude, color='green', s=17) #scatter plot generated on image 
# Customize the plot
plt.title('Distribution of GROW Sensors in the United Kingdom and Ireland')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
#ensures only good values (values within the bounds can be displayed)
#adjust this and extent for different bounds
plt.xlim(-10.592, 1.6848)
plt.ylim(50.681, 57.985)

#displays the plot
# plt.show()

# Check if the file already exists
outputFileName = 'Amediku_GROWSensorLocations_plot.jpeg'
if os.path.exists(outputFileName):
    # If it exists, remove it to save the new version (overwrite)
    os.remove(outputFileName)

# Save the plot in the current directory
generatedFigure.savefig(outputFileName)

# Display a message indicating the successful save
print(f"Plot saved as {outputFileName}")
