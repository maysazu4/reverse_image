from single_thread import *
from multi_process import *




if __name__ == "__main__":
    image_path = "img1.jpg"
    output_path_single = "output_image_single_thread.jpg"
    output_path_multi = "output_image_multi_process.jpg"


    # Single thread/process
    time_single = process_image_single_thread(image_path, output_path_single)
    print("Time taken (single thread):", time_single)

    # Multi process
    time_multi = reverse_image(image_path, output_path_multi)
    print("Time taken (multi process):", time_multi)
