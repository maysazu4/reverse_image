from PIL import Image
import time
from utils import *
import concurrent.futures


def reverse_image(image_path, output_path):
    start_time = time.time()  # Start time measurement
    # Open the image
    with Image.open(image_path) as img:
        # Get image size and pixel data
        width, height = img.size
        pixels = list(img.getdata())

        # Split the pixel data into rows
        rows = [pixels[i*width:(i+1)*width] for i in range(height)]

        # Process each row in parallel using multithreading
        with concurrent.futures.ProcessPoolExecutor() as executor:
            reversed_rows = list(executor.map(reverse_row, rows))

        # Flatten the list of reversed rows
        reversed_pixels = [pixel for row in reversed_rows for pixel in row]

        # Create a new image with the reversed pixel values
        reversed_img = Image.new('RGB', (width, height))
        reversed_img.putdata(reversed_pixels)

        # Save the new reversed image
        reversed_img.save(output_path)
    end_time = time.time()  # End time measurement
    time_taken = end_time - start_time
    return time_taken