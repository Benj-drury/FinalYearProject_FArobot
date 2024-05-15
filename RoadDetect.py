#Road Detection Code - Version 2 - function


import cv2
import numpy as np

def identify_path(webcam, path_number):
  """
  This function identifies a specific path (by number) in a live webcam feed of the racetrack and returns its bounding rectangle.

  Args:
      webcam: A cv2.VideoCapture object representing the webcam.
      path_number: The integer representing the desired path (1-based indexing).

  Returns:
      (x, y, w, h) of the bounding rectangle for the specified path, or None if not found. 
      Where (x, y) represent the coordinates of the rectangle and (w, h) represent the width and height of the rectangle.
  """

  # check for valid path number (1-based indexing)
  if path_number < 1:
      print("Invalid path number (must be 1 or greater)")
      return None

  while True:
    # capture frame from webcam
    ret, frame = webcam.read()
    if not ret:
      print("Error capturing frame!")
      break

    # process the frame to identify paths
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)  
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours by area (largest first)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # check if enough contours are available
    if len(contours) < path_number:
        print(f"Not enough contours found to identify path {path_number}")
        return None

    # get desired path's contour
    cnt = contours[path_number - 1]  # adjust for 0-based indexing

    area = cv2.contourArea(cnt)
    hull = cv2.convexHull(cnt)

    # check if hull_area is non-zero before division
    if cv2.contourArea(hull) > 0:
        convexity = float(area) / cv2.contourArea(hull)  # calculate convexity
    else:
        convexity = 1.0

    if area > 100 and convexity > 0.4:  
      # get bounding rectangle
      x, y, w, h = cv2.boundingRect(cnt)
      print("path ", path_number, " bounded\n")
      return x, y, w, h  # return rectangle coordinates


  return None  # if loop exits without finding the path

