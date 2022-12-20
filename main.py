#!/usr/bin/python3

import PIL
from PIL import Image
import os

while True:
    file_path = input("Enter image file path: ")
    ext = os.path.splitext(file_path)[-1].lower()
    pil_image = PIL.Image.open(file_path)
    if ext == ".png":
        pilimg = PIL.Image.open(file_path)
        wid, hei = pilimg.size
        image_res = str(wid)+"x"+str(hei)
        if image_res == "100x100":
            break
        else:
            print()
            print("Image must be 100x100 pixels.")
    else:
        print()
        print("Invalid file. Select a .png image.")

pixelarray = [0, 0]

color0 = []
color1 = []
color2 = []
color3 = []
color4 = []
color5 = []

while pixelarray <= [99, 99]:
    current_pixel = (pixelarray[0], pixelarray[1])
    pixel_color = pil_image.getpixel(current_pixel)
    if pixel_color[0] >= 0 and pixel_color[0] <= 42:
        color0.append(current_pixel)
        print("appended1")
    elif pixel_color[0] >= 43 and pixel_color[0] <= 84:
        color1.append(current_pixel)
        print("appended2")
    elif pixel_color[0] >= 85 and pixel_color[0] <= 126:
        color2.append(current_pixel)
    elif pixel_color[0] >= 127 and pixel_color[0] <= 168:
        color3.append(current_pixel)
    elif pixel_color[0] >= 168 and pixel_color[0] <= 210:
        color4.append(current_pixel)
    elif pixel_color[0] >= 211 and pixel_color[0] <= 255:
        color5.append(current_pixel)

    if pixelarray[0] < 99:
        pixelarray[0] += 1
    elif pixelarray[1] == 99:
        break
    else:
        pixelarray[1] += 1
        pixelarray[0] = 0

    print(pixelarray)

print("------------------------ color0 ------------------------")
print(color0)
print()

print("------------------------ color1 ------------------------")
print(color1)
print()

print("------------------------ color2 ------------------------")
print(color2)
print()

print("------------------------ color3 ------------------------")
print(color3)
print()

print("------------------------ color4 ------------------------")
print(color4)
print()

print("------------------------ color5 ------------------------")
print(color5)
print()
