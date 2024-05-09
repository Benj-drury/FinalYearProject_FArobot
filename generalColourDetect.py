# Colour Detection Code - Version 4 - function

import cv2
import numpy as np

def detect_objects_in_lanes(webcam, paths):
    """
    This function detects objects and cars in specified lanes of a racetrack using a live webcam feed.

    Args:
        webcam: A cv2.VideoCapture object representing the webcam.
        paths: A list of tuples containing (x, y, w, h) representing the bounding rectangle for each lane.

    Returns:
        A tuple containing flags indicating the presence of objects in each lane.
        A tuple containing flags indicating the presence of car at specific turns.
    """
    # read frame from webcam
    _, imageFrame = webcam.read()

    # convert frame to HSV color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # define range for yellow color and create its mask
    yellow_lower = np.array([20, 100, 100], np.uint8)
    yellow_upper = np.array([30, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    # define range for red color and create its mask
    red_lower = np.array([0, 100, 100], np.uint8)
    red_upper = np.array([10, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # apply morphological transformations to masks
    kernal = np.ones((5, 5), "uint8")
    yellow_mask = cv2.dilate(yellow_mask, kernal)
    red_mask = cv2.dilate(red_mask, kernal)

    # initialize flags for object presence and turns
    object_in_lanes = [False] * len(paths)
    cars_at_turns = [False] * (len(paths) - 1)

    for i, path in enumerate(paths):
        x, y, w, h = path
        
        # find contours for objects
        contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 600:
                Object_X, Object_Y, Object_W, Object_H = cv2.boundingRect(contour)
                imageFrame = cv2.rectangle(imageFrame, (Object_X, Object_Y), (Object_X + Object_W, Object_Y + Object_H),
                                          (0, 0, 255), 2)
                
                ObjCentre_X = (Object_X + Object_W / 2) 
                ObjCentre_Y = (Object_Y + Object_H / 2)

                cv2.putText(imageFrame, f"Object: ({Object_X}, {Object_Y})", (Object_X, Object_Y),
                        cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255))


                # object location analysis
                if (x < ObjCentre_X < x + w) and (y < ObjCentre_Y < y + h):
                    object_in_lanes[i] = True

    # find contours for yellow cars
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 600:
            Object_X, Object_Y, Object_W, Object_H = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (Object_X, Object_Y), (Object_X + Object_W, Object_Y + Object_H),
                                       (0, 199, 255), 2)

            Obj_X = Object_X + Object_W -15
            Obj_Y = Object_Y + Object_H

            cv2.putText(imageFrame, f"Car: ({Object_X}, {Object_Y})", (Obj_X, Obj_Y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 199, 255))
            cv2.putText(imageFrame, "+", (int(Obj_X), int(Obj_Y)), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

            # car location analysis
            for i in range(len(paths) - 1):
                turn_x, turn_y, turn_w, turn_h = paths[0]
                turn_x2, turn_y2, turn_w2, turn_h2 = paths[i+1]
                if (turn_x2 - 50 < Object_X + Object_W/2 < turn_x2 + 50) and (turn_y < Object_Y + Object_H/2 < turn_y + turn_h):
                    cars_at_turns[i] = True

    # draw bounding rectangles for lanes and turns
    for i, path in enumerate(paths):
        x, y, w, h = path
        imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (170, 170, 255), 2)  # Lane
        cv2.putText(imageFrame, f"Path {i+1}", (x+10, y+25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
        if i < len(paths) - 1:
            turn_x, turn_y, turn_w, turn_h = paths[0]
            turn_x2, turn_y2, turn_w2, turn_h2 = paths[i+1]
            imageFrame = cv2.rectangle(imageFrame, (turn_x2 - 50, turn_y), (turn_x2 + 50, turn_y + turn_h),
                                       (0, 255, 127), 4)  # Turn

    # display image with detected objects
    cv2.imshow("Object Detection", imageFrame)

    # return flags indicating object presence in each lane and cars at specific turns
    return tuple(object_in_lanes), tuple(cars_at_turns)
