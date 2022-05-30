# -*- coding: utf-8 -*-
"""Day_Night_Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h0tralxNtrQtcUbbckawNvWf3AYUxPnq
"""

# Importing modules
from PIL import Image
import numpy as np  

# open image file
im = Image.open(r"/content/7.jpg") 
  
# View the image
display(im)

# Function to determine the image as Day or Night
def img_label(img, thrshld):
    is_light = np.mean(img) > thrshld
    return 'Day' if is_light else 'Night'

print(img_label(im, 100))