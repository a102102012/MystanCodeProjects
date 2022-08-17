"""
File: best_photoshop_award.py
Name: Sue Lin
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""

from simpleimage import SimpleImage
# Controls the threshold of detecting green screen pixel
THRESHOLD = 1

# Controls the upper bound for black pixel
BLACK_PIXEL = 200 #0~765
WHITE_PIXEL = 567
EYES_PIXEL = 600


def main():
    """
    創作理念：原圖是以 Lily 快樂地在草皮玩耍作為純天然綠幕
    快點用 Python 幫我 loop 更多串燒
    隔壁餐桌還有火雞！趕緊跳躍到下一個夢境
    """
    fg = SimpleImage('image_contest/lily01.jpeg')
    bg = SimpleImage('image_contest/food02.jpeg')
    bg.make_as_big_as(fg)
    combined_img_food01 = combine(bg, fg)
    fg2 = SimpleImage('image_contest/lily01.jpeg')
    bg2 = SimpleImage('image_contest/food01.jpeg')
    bg2.make_as_big_as(fg)
    combined_img_food02 = combine(bg2, fg2)
    # combined_img_food02.show()
    reflected = reflect(combined_img_food01,combined_img_food02)
    reflected.show()

def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            # Keep Lily's BLack Flur
            if  total < BLACK_PIXEL:
                pass
                # pixel_bg = bg.get_pixel(x, y)
                # pixel_me.red = pixel_bg.red
                # pixel_me.blue = pixel_bg.blue
                # pixel_me.green = pixel_bg.green
            elif pixel_me.green > avg*THRESHOLD :
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
            elif pixel_me.blue > avg*THRESHOLD:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
            elif total > EYES_PIXEL:
                pass
            elif total > WHITE_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
            # Keep＄ Lily's body
            elif pixel_me.red > pixel_me.green and pixel_me.green > pixel_me.blue:
                pass
    return me


def reflect(file01, file02):
    """
    :param filename:img
    :return:img
    1. Create the blank image with double height
    2. For each pixel, fill in the original position and mirror position
    """
    img = file01
    img2 = file02
    blank_img = SimpleImage.blank(img.width * 2, img.height)

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
            img2_position = img2.get_pixel(x, y)
            blank_img_mirror_position = blank_img.get_pixel(blank_img.width-1-x, y)
            blank_img_mirror_position.red = img2_position.red
            blank_img_mirror_position.green = img2_position.green
            blank_img_mirror_position.blue = img2_position.blue

    return blank_img


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
