def reverse_pixel(pixel):
    return tuple(255 - value for value in pixel)

def reverse_row(row):
    # Reverse each pixel value in the row
    return [reverse_pixel(pixel) for pixel in row]