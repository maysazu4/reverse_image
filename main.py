from PIL import Image
import time
import multiprocessing
import concurrent.futures

def reverse_pixel(pixel):
    return tuple(255 - value for value in pixel)

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




def reverse_row(row):
    # Reverse each pixel value in the row
    return [reverse_pixel(pixel) for pixel in row]

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






if __name__ == "__main__":
    image_path = "img1.jpg"
    output_path_single = "output_image_single_thread.jpg"
    output_path_multi = "output_image_multi_process.jpg"

    num_processes = multiprocessing.cpu_count()  # Number of CPU cores

    # Single thread/process
    # time_single = process_image_single_thread(image_path, output_path_single)
    # print("Time taken (single thread):", time_single)

    # Multi process
    time_multi = reverse_image(image_path, output_path_multi)
    print("Time taken (multi process):", time_multi)
