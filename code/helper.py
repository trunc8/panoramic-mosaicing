#!/usr/bin/env python

# trunc8 did this

import numpy as np
import cv2
import matplotlib.pyplot as plt

def stitchPairOfImages(query_img, train_img, displayStitchedImage=True):
  ## ORB = Oriented FAST and Rotated BRIEF
  # Initiate ORB detector
  orb = cv2.ORB_create()

  # find the keypoints and descriptors with ORB
  kp1, des1 = orb.detectAndCompute(train_img,None)
  kp2, des2 = orb.detectAndCompute(query_img,None)

  ### REFLECTIONESSAY: Why this order.


  ## BFMatcher = Brute Force Matcher
  # create BFMatcher object
  bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

  # Match descriptors.
  matches = bf.match(des1,des2)

  # Sort them in the order of their distance.
  matches = sorted(matches, key = lambda x:x.distance)
  print(f"Point correspondences before filtering:{len(matches)}")
  top_matches = matches[:20]

  query_pts = np.float32([ kp1[m.queryIdx].pt for m in top_matches])
  train_pts = np.float32([ kp2[m.trainIdx].pt for m in top_matches])

  ## RANSAC = Random Sample Consensus
  H, _ = cv2.findHomography(query_pts, train_pts,
                            method=cv2.RANSAC,
                            ransacReprojThreshold=4)
  # print(H)

  '''
  The result image size needs to be large enough to accomodate the warped
  train_img. So we take the dimensions of the query image
  and call that a block. Imagine the result image to be a 5x5 grid of
  individual blocks. The center block would be the offset position for the
  reference(query) image and also pre-multiplied to H before warping the
  train image.
  '''

  query_height = query_img.shape[0]
  query_width = query_img.shape[1]

  scale = 5
  result_height = scale*query_height
  result_width = scale*query_width

  offset = np.array([[ 1 , 0 , (scale//2)*query_width],
                     [ 0 , 1 , (scale//2)*query_height],
                     [ 0 , 0 ,    1    ]])
  offset_H = offset@H


  warped_train_img = cv2.warpPerspective(train_img,
                                         offset_H,
                                         (result_width, result_height)
                                        )
  
  ## COMBINING warped_train_img and query_img
  # Blank base image
  result = np.zeros(warped_train_img.shape, dtype=np.uint8)
  
  # Reference image is inserted unchanged into the center grid
  result[(scale//2)*query_height+1 : (1+scale//2)*query_height+1,
         (scale//2)*query_width+1  : (1+scale//2)*query_width+1] = query_img
  
  # The mask ensures that reference image is not overwritten and stays intact
  mask = (result==0)
  
  # Transformed image is inserted using a mask
  result[mask] = warped_train_img[mask]


  ## CROPPING black borders-
  result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

  contours,hierarchy = cv2.findContours(result_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnt = contours[0]
  x,y,w,h = cv2.boundingRect(cnt)
  cropped_result = result[y:y+h,x:x+w]

  if displayStitchedImage:
    # Show intermediate images
    print("Press 'q' to continue")
    plt.figure(figsize=(20,10))
    plt.title("Stitched image", fontsize=16)
    plt.imshow(cv2.cvtColor(cropped_result, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

  return cropped_result