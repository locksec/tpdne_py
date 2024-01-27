import requests
import argparse
import os
from datetime import datetime
from PIL import Image
from io import BytesIO

# Function to fetch and save an image
def fetch_and_save_image(image_number):
    # Requesting data from the website
    response = requests.get("https://www.thispersondoesnotexist.com")
    
    # Check if the response is successful (HTTP 200 OK)
    if response.status_code == 200:
        # Open the image using PIL and convert the response content into a byte stream
        image = Image.open(BytesIO(response.content))
        width, height = image.size  # Extracting image dimensions

        # Defining the area to crop (removing 20 pixels from the bottom)
        crop_area = (0, 0, width, height - 20) 
        cropped_image = image.crop(crop_area)  # Cropping the image

        # Ensuring the 'images' directory exists. Creates it if not present
        os.makedirs('images', exist_ok=True)

        # Creating a unique filename with a timestamp and saving in 'images' directory
        filename = f"images/image_{image_number}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
        cropped_image.save(filename)  # Saving the cropped image
        print(f"Saved {filename}")  # Confirmation message
    else:
        print("Failed to fetch image")  # Error handling if the fetch fails

# Main function to parse arguments and initiate the image fetching process
def main():
    parser = argparse.ArgumentParser()
    # Adding a command-line argument to specify the number of images to fetch
    parser.add_argument("-n", type=int, default=1, help="Number of images to fetch")
    args = parser.parse_args()

    # Looping to fetch the specified number of images
    for i in range(args.n):
        fetch_and_save_image(i)

# Standard Python idiom to execute the main function
if __name__ == "__main__":
    main()
