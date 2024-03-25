# Image Processing Task

## Description
This program processes an image by reversing the RGB values of each pixel. It provides two implementations: one using a single thread/process and another using multiple processes for parallelization.

## Requirements
- Python 3.x
- PIL (Python Imaging Library)
- NumPy (for advanced array manipulation, optional)

## Usage
1. **Single Thread/Process:**
    ```bash
    python single_thread.py input_image.jpg output_image_single_thread.jpg
    ```
    - `input_image.jpg`: Path to the input image file.
    - `output_image_single_thread.jpg`: Path to save the modified image with reversed RGB values.

2. **Multiple Processes:**
    ```bash
    python multi_process.py input_image.jpg output_image_multi_process.jpg
    ```
    - `input_image.jpg`: Path to the input image file.
    - `output_image_multi_process.jpg`: Path to save the modified image with reversed RGB values.

## Performance
- The performance of both implementations can be compared by observing the time taken for processing the image.
- The multi-process implementation is expected to demonstrate a speed improvement over the single-threaded approach, especially on multi-core systems.

## Notes
- Make sure to replace `"input_image.jpg"` with the path to your input image file.
- Ensure that you have necessary permissions to read from and write to the specified image files.
- For optimal performance, consider running the multi-process implementation on a system with multiple CPU cores.

## References
- [PIL Documentation](https://pillow.readthedocs.io/en/stable/)
- [Multiprocessing Documentation](https://docs.python.org/3/library/multiprocessing.html)
