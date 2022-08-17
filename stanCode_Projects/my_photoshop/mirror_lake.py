"""
File: mirror_lake.py
Name: Sue Lin
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:img
    :return:img
    1. Create the blank image with double height
    2. For each pixel, fill in the original position and mirror position
    """
    img = SimpleImage(filename)

    blank_img = SimpleImage.blank(img.width, img.height * 2)

    for x in range(img.width):
        for y in range(img.height):
            # Scan the original image
            img_position = img.get_pixel(x, y)
            # Replace blank (x,y) with original image's pixel
            blank_img_original_position = blank_img.get_pixel(x,y)
            blank_img_original_position.red = img_position.red
            blank_img_original_position.green = img_position.green
            blank_img_original_position.blue = img_position.blue

            # Replace blank (x,y) with original image's pixel
            blank_img_mirror_position = blank_img.get_pixel(x, blank_img.height-1-y)
            blank_img_mirror_position.red = img_position.red
            blank_img_mirror_position.green = img_position.green
            blank_img_mirror_position.blue = img_position.blue

    return blank_img

def main():
    """
    Input an image, reflect it, and show it.
    """
    # original_mt = SimpleImage('images/mt-rainier.jpg')
    # original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
