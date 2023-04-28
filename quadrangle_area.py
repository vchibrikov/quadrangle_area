#import packages

import os
import cv2
import pandas as pd
import math

# Create an empty DataFrame to store the results
df = pd.DataFrame(columns=['file_name', 'area_pixels'])
output_filename = 'test_data.csv'


# Define the function to handle mouse events
def mouse_callback(event, x, y, flags, params):

    # If left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN and len(params['points']) < 4:

        # Add the point to the list
        params['points'].append((x, y))

        # Draw a circle at the point
        cv2.circle(params['image'], (x, y), 5, (0, 0, 255), -1)

        # Update the display
        cv2.imshow("image", params['image'])

        # draw line
        if len(params['points']) == 2:

             # Define the points
            point1 = params['points'][-2]
            point2 = params['points'][-1]  
        
            # Draw a line between the points
            cv2.line(params['image'], point1, point2, (0, 0, 255), 2)

            # Update the display
            cv2.imshow('image', params['image'])

        # draw line
        if len(params['points']) == 3:

             # Define the points
            point1 = params['points'][-2]
            point2 = params['points'][-1]  
        
            # Draw a line between the points
            cv2.line(params['image'], point1, point2, (0, 0, 255), 2)

            # Update the display
            cv2.imshow('image', params['image'])

        # If four points have been selected, calculate the area
        if len(params['points']) == 4:

            # Define the points
            point1 = params['points'][-2]
            point2 = params['points'][-1]
            point3 = params['points'][-4]
        
            # Draw a line between the points
            cv2.line(params['image'], point1, point2, (0, 0, 255), 2)
            cv2.line(params['image'], point3, point2, (0, 0, 255), 2)

            # Update the display
            cv2.imshow('image', params['image'])

            # Define the sides of the quadrangle and dialonals
            AB = ((params['points'][0][0]-params['points'][1][0])**2 + (params['points'][0][1]-params['points'][1][1])**2)**0.5
            BC = ((params['points'][1][0]-params['points'][2][0])**2 + (params['points'][1][1]-params['points'][2][1])**2)**0.5
            CD = ((params['points'][2][0]-params['points'][3][0])**2 + (params['points'][2][1]-params['points'][3][1])**2)**0.5
            DA = ((params['points'][3][0]-params['points'][0][0])**2 + (params['points'][3][1]-params['points'][0][1])**2)**0.5
            AC = ((params['points'][0][0]-params['points'][2][0])**2 + (params['points'][0][1]-params['points'][2][1])**2)**0.5
            BD = ((params['points'][1][0]-params['points'][3][0])**2 + (params['points'][1][1]-params['points'][3][1])**2)**0.5

            # Define half perimeter
            S = (AB + BC + CD + DA)/2

            # # Calculate the area of the quadrangle in pixels according to Bretschneider's Formula
            A = math.sqrt((S-AB)*(S-BC)*(S-CD)*(S-DA) - 0.25*(AB*CD+BC*DA+AC*BD)*(AB*CD+BC*DA-AC*BD))

            # add data to dataframe and export
            df.loc[len(df)] = [filename_short, A]
            df.to_csv(path + output_filename, index = False)

# Define the folder containing the images
folder = '/Users/---/Desktop/---/---/---/' 
path = '/Users/---/Desktop/---/---/---/'

# Define the extensions of the image files
extensions = ('.jpeg','.tiff', '.jpg', '.tif')

# Iterate over the images in the folder
for filename in os.listdir(folder):
    if filename.lower().endswith(extensions):

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






