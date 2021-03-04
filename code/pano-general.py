#!/usr/bin/env python

# trunc8 did this

import numpy as np
import cv2
import matplotlib.pyplot as plt

import os, sys

from helper import stitchPairOfImages

# directory = path-to-directory-containing-n-images
# referenceImage = index of input image to be kept intact

if len(sys.argv) < 2:
  # default, if no arguments are passed
  directory = os.path.join(sys.path[0], "../data/general/mountain")
  referenceImage = 3
else:
  directory = sys.argv[1]
  referenceImage = int(sys.argv[2])

images = [f for f in os.listdir(directory) if 
          os.path.isfile(os.path.join(directory,f))]
images.sort()

if (referenceImage > len(images)):
  print("Invalid reference image entered. Defaulting to first image.")
  referenceImage = 1

# Query = Reference image
# Train = Transform image


def generalParanoma(images, referenceImage):
  num_images = len(images)
  index = referenceImage-1
  
  query_img_path = os.path.join(directory, images[index])
  query_img = cv2.imread(query_img_path)
  

  left_index = index - 1 # iterate leftwards through sequence
  right_index = index + 1 # iterate rightwards through sequence
  for i in range(1,num_images):
    # first stitch all left images till the start
    if left_index >= 0:
      train_img_index = left_index
      left_index = left_index - 1
    # then stitch right images
    elif right_index < num_images:
      train_img_index = right_index
      right_index = right_index + 1
    else:
      break
    
    # new image to be read and stitched into existing mosaic image
    train_img_path = os.path.join(directory, images[train_img_index])
    train_img = cv2.imread(train_img_path)

    if i == num_images-1:
      print("\t\tFINAL PANAROMA IMAGE...")
    query_img = stitchPairOfImages(query_img, train_img, displayStitchedImage=True)

  result = query_img # Resulting mosaic image
  return result


result = generalParanoma(images, referenceImage)
## Display panaroma image
# plt.figure(figsize=(20,10))
# plt.title("Result: Panaromic image", fontsize=16)
# plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
# plt.axis('off')
# plt.show()

## Saving final image
if directory[-1] == "/":
  name = directory.split("/")[-2]
else:
  name = directory.split("/")[-1]

if not os.path.exists(f"../results/pano-general-results/{name}"):
  os.makedirs(f"../results/pano-general-results/{name}")

cv2.imwrite(f"../results/pano-general-results/{name}/auto_{name}_ref_{referenceImage}.jpg", result)