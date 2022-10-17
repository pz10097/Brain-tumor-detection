from PIL import Image, ImageFilter
import numpy as np
import os

directory_yes = 'brain_tumor_dataset/yes/'
directory_no = 'brain_tumor_dataset/no/'
k = 50

for image in os.listdir(directory_yes):
    img = Image.open(directory_yes + image)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img1 = img.convert('L')  
    img2 = np.array(img1)
    brain = np.where(img2 >= k)
    top = min(brain[0])
    bottom = max(brain[0])
    left = min(brain[1])
    right = max(brain[1])
    img3 = img.crop((left, top, right, bottom))
    img3.save("brain_tumor_dataset/yes_crop_50_rgb/" + image)



for image in os.listdir(directory_no):
    img = Image.open(directory_no + image)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img1 = img.convert('L')
    img2 = np.array(img1)
    brain = np.where(img2 >= k)
    top = min(brain[0])
    bottom = max(brain[0])
    left = min(brain[1])
    right = max(brain[1])
    img3 = img.crop((left, top, right, bottom))
    img3.save("brain_tumor_dataset/no_crop_50_rgb/" + image)
