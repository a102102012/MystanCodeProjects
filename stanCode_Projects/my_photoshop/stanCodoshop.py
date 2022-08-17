"""
File: stanCodoshop.py
Name: Sue Lin
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    pixel_red = pixel.red
    pixel_green = pixel.green
    pixel_blue = pixel.blue
    ans = math.sqrt((red - pixel_red) ** 2 + (green - pixel_green) ** 2 + (blue - pixel_blue) ** 2)
    return ans


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # input example
    # r:0 g:255 b:0
    # r:0 g:255 b:0
    # r:0 g:255 b:0
    # r:0 g:0 b:255

    red_avg = 0
    green_avg = 0
    blue_avg = 0

    for i in range(len(pixels)):
        red_avg += pixels[i].red
        green_avg += pixels[i].green
        blue_avg += pixels[i].blue
    red_avg = int(red_avg / len(pixels))
    green_avg = int(green_avg / len(pixels))
    blue_avg = int(blue_avg / len(pixels))
    return [red_avg, green_avg, blue_avg]
    # output example = [0, 191, 63]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the
    average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """

    avg = get_average(pixels)
    min_distance = get_pixel_dist(pixels[0], avg[0], avg[1], avg[2])  # default to get the first distance
    min_distance_pixel = pixels[0]
    for i in range(len(pixels)):
        if get_pixel_dist(pixels[i], avg[0], avg[1], avg[2]) < min_distance:
            min_distance = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
            min_distance_pixel = pixels[i]
    return min_distance_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    for x in range(images[0].width):
        for y in range(images[0].height):
            lst_all_images = []
            for i in range(len(images)):
                # to read more than 3 images
                lst_all_images.append(images[i].get_pixel(x, y))
            # best = get_best_pixel([images[0].get_pixel(x, y), images[1].get_pixel(x, y), images[2].get_pixel(x,y)])
            best = get_best_pixel(lst_all_images)
            result.get_pixel(x, y).red = best.red
            result.get_pixel(x, y).green = best.green
            result.get_pixel(x, y).blue = best.blue

    # Test Set milestone 1
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # Test Set milestone 2
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # Test Set milestone 3
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """

    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
