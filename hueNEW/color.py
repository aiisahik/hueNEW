# -*- compile-command: "python color.py" -*-

import Image

def find_color(region):
    region = region.point(lambda i: i / 4)
    w = region.getcolors(region.size[0] * region.size[1]);
    color = max(w)[1]
    color = (color[0]*4,color[1]*4,color[2]*4) #region.getpixel(box) 
    print color
    return color

def get_box (center, width, height):
    x = center[0]    
    y = center[1]    
    x = x - width / 2
    y = y - height / 2
    return (x, y, x+width, y+height)

def save_color (color, name):
    im = Image.new("RGB", (100,100), color)
    im.save(name)

def get_colors (im):
    width = im.size[0]/5;
    height = width * 3;
    color = [0,0,0]

    point = (im.size[0]/2, im.size[1]/2) # center
    box = get_box(point, width, height)  # width x height
    region = im.crop(box)
    region.save("square0.jpg")
    color[0] = find_color(region)
    save_color(color[0], "color0.jpg")

    point = (im.size[0]/2, im.size[1]/2 - width * 3 / 2) # top
    box = get_box(point, width, width)  # width x width
    region = im.crop(box)
    region.save("square1.jpg")
    color[1] = find_color(region)
    save_color(color[1], "color1.jpg")

    point = (im.size[0]/2, im.size[1]/2 + width * 3 / 2) # bottom
    box = get_box(point, width, width)  # width x width
    region = im.crop(box)
    region.save("square2.jpg")
    color[2] = find_color(region)
    save_color(color[2], "color2.jpg")
    return color


im = Image.open("sample.jpg")
color = get_colors(im)
print color



