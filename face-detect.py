# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 00:46:42 2018

@author: Aman Singh
@mail: amansingh9097@gmail.com
"""

import cv2


# Get image path as argument
imagePath = "abba.png"
cascPath = "haarcascade_frontalface_default.xml"

# create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# load image, convert to grayscale
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in image
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags= cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow("Faces found", image)
cv2.waitKey(0)