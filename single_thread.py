from PIL import Image
import time
from utils import *
def process_image_single_thread(image_path, output_path):
    start_time = time.time()

    # Open the image
    with Image.open(image_path) as img:
        # Create a new image object to store the modified pixels
        new_img = Image.new('RGB', img.size)

        # Iterate over each pixel and reverse its values
        width, height = img.size
        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                reversed_pixel = reverse_pixel(pixel)
                new_img.putpixel((x, y), reversed_pixel)

        # Save the new reversed image
        new_img.save(output_path)

    end_time = time.time()
    return end_time - start_time