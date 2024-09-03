"""
based on:
https://stackoverflow.com/a/451580/6631639
https://kanoki.org/2017/07/12/merge-images-with-python/
https://stackoverflow.com/a/16377244/6631639
https://stackoverflow.com/a/41887497/6631639
"""

import numpy as np
from PIL import Image, ImageFont, ImageDraw
import os
import img2pdf

def change_height_proportionally(img, width):
    """Change height of image proportional to given width."""
    wpercent = width / img.size[0]
    proportional_height = int(img.size[1] * wpercent)
    return img.resize((width, proportional_height), Image.ANTIALIAS)


def change_width_proportionally(img, height):
    """Change width of image proportional to given height."""
    hpercent = height / img.size[1]
    proportional_width = int(img.size[0] * hpercent)
    return img.resize((proportional_width, height), Image.ANTIALIAS)


def make_same_width(image_list):
    """Make all images in input list the same width."""
    imgs = [Image.open(i) for i in image_list]
    min_width = min([i.size[0] for i in imgs])
    resized = [change_height_proportionally(img, min_width) for img in imgs]
    return [np.asarray(i) for i in resized]


def make_same_height(image_list):
    """Make all images in input list the same height."""
    imgs = [Image.open(i) for i in image_list]
    min_height = min([i.size[1] for i in imgs])
    resized = [change_width_proportionally(img, min_height) for img in imgs]
    return [np.asarray(i) for i in resized]


def add_text(img):
    """Add text annotation to hardcoded locations."""
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",
        size=24,
        encoding="unic")
    draw = ImageDraw.Draw(img)
    draw.text((30, 30), "A", (0, 0, 0), font=font)
    draw.text((30, 490), "B", (0, 0, 0), font=font)
    draw.text((30, 950), "C", (0, 0, 0), font=font)
    draw.text((30, 1430), "D", (0, 0, 0), font=font)
    draw.text((510, 30), "E", (0, 0, 0), font=font)
    draw.text((510, 950), "F", (0, 0, 0), font=font)


def main():
    for i in range(50,77):
        simTag = f'ASG_{i}'
        fileFolder = '/media/adamlab/My Passport/CARLsim6_surrogate_gradient/data_archive/combined_analysis_images/'

        hidOutChangeDist = fileFolder+simTag+'_hid-out_change_dist.png'
        hidOutFinalDist = fileFolder+simTag+'_hid-out_final_dist.png'
        inHidChangeDist = fileFolder+simTag+'_in-hid_change_dist.png'
        inHidFinalDist = fileFolder+simTag+'_in-hid_final_dist.png'

        Image.fromarray(np.hstack(make_same_height([inHidFinalDist,hidOutFinalDist]))).save('finalDist.png')
        Image.fromarray(np.hstack(make_same_height([inHidChangeDist,hidOutChangeDist]))).save('changeDist.png')
        Image.fromarray(np.vstack(make_same_width(['finalDist.png','changeDist.png']))).save('dist.png')


        class0Example = fileFolder+simTag+'_sampleVoltage_e19_b30_class0_case18.png'
        class1Example = fileFolder+simTag+'_sampleVoltage_e19_b30_class1_case254.png'
        class2Example = fileFolder+simTag+'_sampleVoltage_e19_b30_class2_case3.png'
        Image.fromarray(np.hstack(make_same_height([class0Example, class1Example, class2Example]))).save('examples.png')

        Image.fromarray(np.vstack(make_same_width(['dist.png','examples.png']))).save(f'{simTag}_combined.png')
        image = Image.open(f'{simTag}_combined.png')
 
        pdf_bytes = img2pdf.convert(image.filename)
 
        # opening or creating pdf file
        file = open(f'{simTag}_combined.pdf', "wb")
         
        # writing pdf files with chunks
        file.write(pdf_bytes)
         
        # closing image file
        image.close()
         
        # closing pdf file
        file.close()

        inHidWeight = fileFolder+simTag+'_in-hid_weight_traj.png'
        hidOutWeight = fileFolder+simTag+'_hid-out_weight_traj.png'
        image = Image.open(inHidWeight)
        w,h = image.size
        imageCropped = image.crop((0,0,w,int(h*0.3))).save('in-hid_traj.png')
        Image.fromarray(np.vstack(make_same_width(['in-hid_traj.png',hidOutWeight]))).save(f'{simTag}_trajectory.png')
        image = Image.open(f'{simTag}_trajectory.png')
 
        pdf_bytes = img2pdf.convert(image.filename)
 
        # opening or creating pdf file
        file = open(f'{simTag}_trajectory.pdf', "wb")
         
        # writing pdf files with chunks
        file.write(pdf_bytes)
         
        # closing image file
        image.close()
         
        # closing pdf file
        file.close()

    combined = Image.fromarray(np.hstack(make_same_height(["left.png", "right.png"])))
    add_text(combined)
    combined.save('Combined_images.png', pi=combined.size)
    [os.remove(f) for f in ["left.png", "right.png"]]


if __name__ == '__main__':
    main()
