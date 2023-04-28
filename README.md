# quadrangle_area.py

This Python script is designed to calculate the area of a quadrangle based on Bretschneider's formula. The script takes in an image file path, prompts the user to select four points to define the quadrangle, and then calculates the area of the quadrangle using the selected points. The area of the quadrangle is then added to a Pandas dataframe and exported to a CSV file.

# Prerequisites

-   Python 3.x
-   OpenCV 4.x
-   Pandas

# Installation

-   Install Python 3.x from the official website.
-   Install OpenCV 4.x using pip:

pip install opencv-python-headless

-   Install Pandas using pip:

pip install pandas

-   Download the script and save it to a directory of your choice.

# Usage

-   Modify the following lines of the script to specify the folder containing your images (flder) and the folder where your output file will be stored (output):

folder = '/Users/---/Desktop/---/---' 

path = '/Users/---/Desktop/---/---/'

-   Modify the following line of the script to specify the file extensions of your image files:

extensions = ('.jpeg','.tiff', '.jpg', '.tif')

-   Run the script from the command line using the following command:

python quadrangle_area.py

- The script will prompt you to select four points to define the quadrangle in each image. Select the points by clicking on the image, and press any key to continue to the next image. The area of the quadrangle will be added to a Pandas dataframe and exported to a CSV file.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
