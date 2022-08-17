"""
File: blur.py
Name: Sue Lin
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:img
    :return:img
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)


    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            # Todo: get pixel of new_img at x,y
            new_img_position = new_img.get_pixel(x, y)
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x+1, y+0)
                avg_2 = img.get_pixel(x+1, y+1)
                avg_3 = img.get_pixel(x+0, y+1)
                new_img_position.blue = (center.blue+avg_1.blue+avg_2.blue+avg_3.blue)//4
                new_img_position.green = (center.green+avg_1.green+avg_2.green+avg_3.green)//4
                new_img_position.red = (center.red+avg_1.red+avg_2.red+avg_3.red)//4
           

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x-1, y+0)
                avg_2 = img.get_pixel(x-1, y+1)
                avg_3 = img.get_pixel(x+0, y+1)
                new_img_position.blue = (center.blue+avg_1.blue+avg_2.blue+avg_3.blue)//4
                new_img_position.green = (center.green+avg_1.green+avg_2.green+avg_3.green)//4
                new_img_position.red = (center.red+avg_1.red+avg_2.red+avg_3.red)//4

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x+1, y+0)
                avg_2 = img.get_pixel(x+1, y-1)
                avg_3 = img.get_pixel(x+0, y-1)
                new_img_position.blue = (center.blue+avg_1.blue+avg_2.blue+avg_3.blue)//4
                new_img_position.green = (center.green+avg_1.green+avg_2.green+avg_3.green)//4
                new_img_position.red = (center.red+avg_1.red+avg_2.red+avg_3.red)//4

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x-1, y-1)
                avg_2 = img.get_pixel(x+0, y-1)
                avg_3 = img.get_pixel(x-1, y+0)
                new_img_position.blue = (center.blue+avg_1.blue+avg_2.blue+avg_3.blue)//4
                new_img_position.green = (center.green+avg_1.green+avg_2.green+avg_3.green)//4
                new_img_position.red = (center.red+avg_1.red+avg_2.red+avg_3.red)//4
 
            elif y == 0:
                # Get top edge's pixels (without two corners)
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x-1, y+0)
                avg_2 = img.get_pixel(x-1, y+1)
                avg_3 = img.get_pixel(x+0, y+1)
                avg_4 = img.get_pixel(x+1, y+0)
                avg_5 = img.get_pixel(x+1, y+1)
                new_img_position.blue = (center.blue+avg_1.blue+avg_2.blue+avg_3.blue+avg_4.blue+avg_5.blue)//6
                new_img_position.green = (center.green+avg_1.green+avg_2.green+avg_3.green+avg_4.green+avg_5.green)//6
                new_img_position.red = (center.red+avg_1.red+avg_2.red+avg_3.red+avg_4.red+avg_5.red)//6

            elif y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x-1, y-1)
                avg_2 = img.get_pixel(x-1, y+0)
                avg_3 = img.get_pixel(x+0, y-1)
                avg_4 = img.get_pixel(x+1, y+0)
                avg_5 = img.get_pixel(x+1, y-1)
                new_img_position.blue = (center.blue+avg_1.blue+avg_2.blue+avg_3.blue+avg_4.blue+avg_5.blue)//6
                new_img_position.green = (center.green+avg_1.green+avg_2.green+avg_3.green+avg_4.green+avg_5.green)//6
                new_img_position.red = (center.red+avg_1.red+avg_2.red+avg_3.red+avg_4.red+avg_5.red)//6

            elif x == 0:
                # Get left edge's pixels (without two corners)
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x - 0, y - 1)
                avg_2 = img.get_pixel(x - 0, y + 1)
                avg_3 = img.get_pixel(x + 1, y + 1)
                avg_4 = img.get_pixel(x + 1, y + 0)
                avg_5 = img.get_pixel(x + 1, y - 1)
                new_img_position.blue = (center.blue + avg_1.blue + avg_2.blue + avg_3.blue + avg_4.blue + avg_5.blue) // 6
                new_img_position.green = (center.green + avg_1.green + avg_2.green + avg_3.green + avg_4.green + avg_5.green) // 6
                new_img_position.red = (center.red + avg_1.red + avg_2.red + avg_3.red + avg_4.red + avg_5.red) // 6

            elif x == img.width-1:
                # Get right edge's pixels (without two corners)
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x - 0, y - 1)
                avg_2 = img.get_pixel(x - 0, y + 1)
                avg_3 = img.get_pixel(x - 1, y + 1)
                avg_4 = img.get_pixel(x - 1, y + 0)
                avg_5 = img.get_pixel(x - 1, y - 1)
                new_img_position.blue = (center.blue + avg_1.blue + avg_2.blue + avg_3.blue + avg_4.blue + avg_5.blue) // 6
                new_img_position.green = (center.green + avg_1.green + avg_2.green + avg_3.green + avg_4.green + avg_5.green) // 6
                new_img_position.red = (center.red + avg_1.red + avg_2.red + avg_3.red + avg_4.red + avg_5.red) // 6

            else:
                # Inner pixels
                center = img.get_pixel(x, y)
                avg_1 = img.get_pixel(x - 0, y - 1)
                avg_2 = img.get_pixel(x - 0, y + 1)
                avg_3 = img.get_pixel(x - 1, y + 1)
                avg_4 = img.get_pixel(x - 1, y + 0)
                avg_5 = img.get_pixel(x - 1, y - 1)
                avg_6 = img.get_pixel(x + 1, y + 1)
                avg_7 = img.get_pixel(x + 1, y + 0)
                avg_8 = img.get_pixel(x + 1, y - 1)
                new_img_position.blue = (center.blue + avg_1.blue + avg_2.blue + avg_3.blue +
                                         avg_4.blue + avg_5.blue + avg_6.blue + avg_7.blue + avg_8.blue) // 9
                new_img_position.green = (center.green + avg_1.green + avg_2.green + avg_3.green +
                                          avg_4.green + avg_5.green + avg_6.green + avg_7.green + avg_8.green) // 9
                new_img_position.red = (center.red + avg_1.red + avg_2.red + avg_3.red +
                                        avg_4.red + avg_5.red + avg_6.red + avg_7.red + avg_8.red) // 9


    return new_img


def main():
    """
    Read the image
    Blur the image with loop
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
