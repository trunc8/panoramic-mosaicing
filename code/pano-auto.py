#!/usr/bin/env python

# trunc8 did this

import numpy as np
import cv2
import matplotlib.pyplot as plt

import os, sys

from helper import stitchPairOfImages

# directory = path-to-directory-containing-2-images

if len(sys.argv) < 2:
  # default, if no arguments are passed
  directory = os.path.join(sys.path[0], "../data/auto/yard")
else:
  directory = sys.argv[1]

images = [f for f in os.listdir(directory) if 
          os.path.isfile(os.path.join(directory,f))]
images.sort()

# Query = Reference image
# Train = Transform image

is_I2_reference_image = 1 # 0: False, 1: True
if is_I2_reference_image:
  query_img_path = os.path.join(directory, images[1])
  train_img_path = os.path.join(directory, images[0])
else:
  query_img_path = os.path.join(directory, images[0])
  train_img_path = os.path.join(directory, images[1])

query_img = cv2.imread(query_img_path)
train_img = cv2.imread(train_img_path)

## Display query and train images
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,
                               constrained_layout=False,
                               figsize=(16,9))
ax1.imshow(cv2.cvtColor(query_img, cv2.COLOR_BGR2RGB))
ax1.set_title("Reference image", fontsize=14)
ax1.axis('off')

ax2.imshow(cv2.cvtColor(train_img, cv2.COLOR_BGR2RGB))
ax2.set_title("Transform image", fontsize=14)
ax2.axis('off')

plt.suptitle("Input images", fontsize=18)
print("Press 'q' to continue")
plt.show()

## Panaroma algorithm
result = stitchPairOfImages(query_img, train_img,
                            displayStitchedImage=False)

## Display panaroma image
plt.figure(figsize=(20,10))
plt.title("Result: Panaroma image", fontsize=16)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

## Saving final image
if directory[-1] == "/":
  name = directory.split("/")[-2]
else:
  name = directory.split("/")[-1]

if not os.path.exists(f"../results/pano-auto-results/{name}"):
  os.makedirs(f"../results/pano-auto-results/{name}")

if is_I2_reference_image:
  img_name = f"../results/pano-auto-results/{name}/auto_{name}.jpg"
else:
  img_name = f"../results/pano-auto-results/{name}/auto_{name}_I1_reference.jpg"

cv2.imwrite(img_name, result)