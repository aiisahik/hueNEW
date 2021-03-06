# -*- compile-command: "python color.py" -*-

import Image
import os

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
    #region.save("square0.jpg")
    color[0] = find_color(region)
    #save_color(color[0], "color0.jpg")

    point = (im.size[0]/2, im.size[1]/2 - width * 3 / 2) # top
    box = get_box(point, width, width)  # width x width
    region = im.crop(box)
    #region.save("square1.jpg")
    color[1] = find_color(region)
    #save_color(color[1], "color1.jpg")

    point = (im.size[0]/2, im.size[1]/2 + width / 2) # bottom
    box = get_box(point, width, width)  # width x width
    region = im.crop(box)
    #region.save("square2.jpg")
    color[2] = find_color(region)
    #save_color(color[2], "color2.jpg")
    return color




import simplejson as json


fout = open("color.json","w")

for y in range(2012, 2013):
    for m in range(1, 12):
        month = "%d%02d" % (y, m)
        file = "runway"  + month + ".json";
        #print file + "------------"
        f = open(file,"r")

        runway = json.load(f)
        for x in runway["items"]:
            site = x["origin_site_url"]
            creation = x["creation_date"]
            #print creation

            if "pages" in x:
                for page in x["pages"]:
                    if "imagelist" in page:
                        for image in page["imagelist"]:
                            url = site + image["large_url"]
                            os.system("wget -O out.jpg " + url);
                            im = Image.open("out.jpg")
                            color = get_colors(im)
                            record = [ creation, url, color[0] ]
                            buf = json.dumps(record)
                            fout.write(buf + "\n")
                            fout.flush()
                            #print color






#"items": x
#  "origin_site_url" : "http://www.elle.com",
#  "pages" : 
#     "imagelist" : [
#    {

#import fileinput
#for line in fileinput.input():
#    os.system("wget -O out.jpg " + line);
#    im = Image.open("out.jpg")
#    color = get_colors(im)
#    print color
#    os.system("viewnior out.jpg");
#    os.system("viewnior square0.jpg");
#    os.system("viewnior color0.jpg");
#    os.system("viewnior square1.jpg");
#    os.system("viewnior color1.jpg");
#    os.system("viewnior square2.jpg");
#    os.system("viewnior color2.jpg");


#os.system("viewnior sample.jpg");
#im = Image.open("sample.jpg")












            
#$month = sprintf("%02d", $m);
#$file = "runway$y$month.json";


#f = open("runway.json","r")

#runway = json.load(f)
#for x in runway["items"]:
#    site = x["origin_site_url"]
#    creation = x["creation_date"]
#    print creation
#    for page in x["pages"]:
#        if "imagelist" in page:
#            for image in page["imagelist"]:
#                pass #print site + image["large_url"]

