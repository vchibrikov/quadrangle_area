# Calculate quadrangle area according to Bretschneider's Formula

#import packages
import os
import cv2
import pandas as pd
import math

# Create an empty data frame to store the results
df = pd.DataFrame(columns=['file_name', 'area_pixels'])

# Define a name of file in which data will be exported
output_filename = 'test_data.csv'

# Define the function to handle mouse events
def mouse_callback(event, x, y, flags, params):

    # If left mouse button is pressed lower than the number of quadrangle corners (4)
    if event == cv2.EVENT_LBUTTONDOWN and len(params['points']) < 4:

        # Add the coordinates of the respected point to the list
        params['points'].append((x, y))

        # Draw a circle at the point
        cv2.circle(params['image'], (x, y), 5, (0, 0, 255), -1)

        # Update the display so that previously clicked corner will be visible
        cv2.imshow("image", params['image'])

        # If four points have been selected, calculate the area
        if len(params['points']) == 4:

            # Define the sides of the quadrangle and its diagonals
            AB = ((params['points'][0][0]-params['points'][1][0])**2 + (params['points'][0][1]-params['points'][1][1])**2)**0.5
            BC = ((params['points'][1][0]-params['points'][2][0])**2 + (params['points'][1][1]-params['points'][2][1])**2)**0.5
            CD = ((params['points'][2][0]-params['points'][3][0])**2 + (params['points'][2][1]-params['points'][3][1])**2)**0.5
            DA = ((params['points'][3][0]-params['points'][0][0])**2 + (params['points'][3][1]-params['points'][0][1])**2)**0.5
            AC = ((params['points'][0][0]-params['points'][2][0])**2 + (params['points'][0][1]-params['points'][2][1])**2)**0.5
            BD = ((params['points'][1][0]-params['points'][3][0])**2 + (params['points'][1][1]-params['points'][3][1])**2)**0.5

            # # Define half perimeter of quadrangle 
            S = (AB + BC + CD + DA)/2

            # # Calculate the area of the quadrangle in pixels according to Bretschneider's Formula
            A = math.sqrt((S-AB)*(S-BC)*(S-CD)*(S-DA) - 0.25*(AB*CD+BC*DA+AC*BD)*(AB*CD+BC*DA-AC*BD))

	    # append the results of calculation to dataframe
            df.loc[len(df)] = [filename_short, A]

	    # export dataframe  
            df.to_csv(path + output_filename, index = False)

# Define the folder containing the images
folder = '/Users/---/Desktop/---/---' 
# Define the folder where your output file will be stored
path = '/Users/---/Desktop/---/---/'

# Define the extensions of the image files (optionally to change according to your file format)
extensions = ('.jpeg','.tiff', '.jpg', '.tif')

# Iterate over the images in the folder
for filename in os.listdir(folder):
    if filename.lower().endswith(extensions):

	# remove file format from the filename so in exported file only filename without format will be shown
        filename_short = filename.replace('.tif', '')
        filename_short = filename.replace('.jpeg', '')
        filename_short = filename.replace('.tiff', '')
        filename_short = filename.replace('.jpg', '')

        # Load the image
        image = cv2.imread(os.path.join(folder, filename))

        # Create a copy of the image for display purposes
        display_image = image.copy()
        
        # Define the dictionary of parameters to be passed to the mouse callback function
        params = {'image': display_image, 'filename': filename, 'points': []}
        
        # Create a window to display the image
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        
        # Set the mouse callback function
        cv2.setMouseCallback("image", mouse_callback, params)
        
        # Show the image and wait for user to select points
        cv2.imshow("image", image)
        cv2.setMouseCallback("image", mouse_callback, params)
        cv2.waitKey(0)



