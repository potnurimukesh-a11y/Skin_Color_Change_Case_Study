"""
This program highlights fires in an image by identifying pixels
whose red intensity is more than INTENSITY_THRESHOLD times the
average of the red, green, and blue values at a pixel. Those
"sufficiently red" pixels are then highlighted in the image
and other pixels are turned grey, by setting the pixel red,
green, and blue values to be all the same average value.
"""

from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.0
DEFAULT_FILE = 'images/President-Trump-Official-Portrait.jpg'

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)
            
    # write your logic here
    for pixel in image:
        if pixel.red - pixel.green > 7 and pixel.red - pixel.blue < 90:
            pixel.red = int(pixel.red * 0.75)
            pixel.green = int(pixel.green * 0.70)
            pixel.blue = int(pixel.blue * 0.70)
    return image

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
