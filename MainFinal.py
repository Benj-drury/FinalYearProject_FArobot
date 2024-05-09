##MainFinal.py test file 

import cv2
from generalColourDetect import detect_objects_in_lanes
from LineFollowFunc import driveCar
from RoadDetect import identify_path
from gui import CarStatusGUI

driveCar("Setup")
webcam = cv2.VideoCapture(1)
# define paths using the identify_path function
path1 = identify_path(webcam, 1)
path2 = identify_path(webcam, 2)
path3 = identify_path(webcam, 3)

# construct the paths list
paths = [path1, path2, path3]

gui = CarStatusGUI()

if __name__ == "__main__":
    while True:
        object_in_lanes, car_at_turns = detect_objects_in_lanes(webcam, paths) # call object detection

        # establish flags
        car_turn1 = car_at_turns[0]; car_turn2 = car_at_turns[1]
        object_in_lane1 = object_in_lanes[0]; object_in_lane2 = object_in_lanes[1]; object_in_lane3 = object_in_lanes[2]

        # display the result
        gui.update_values(car_turn1, car_turn2, object_in_lane1, object_in_lane2, object_in_lane3)

        # if/elif checks for car and object location 
        if car_turn1 or car_turn2:
            if object_in_lane1:
                if object_in_lane3 and not object_in_lane2:
                    if car_turn1:
                        driveCar("LeftPath")
                    if car_turn2:
                        driveCar("Stop")
                    else:
                        driveCar("Go")
                elif object_in_lane2 and not object_in_lane3:
                    if car_turn2:
                        if object_in_lane1 and not object_in_lane3:
                            driveCar("RightPath")
                    else:
                        driveCar("Go")
                elif not object_in_lane2 or not object_in_lane3:
                    if car_turn1:
                        driveCar("LeftPath")
                    elif car_turn2:
                        driveCar("RightPath")
                elif (object_in_lane1 and object_in_lane2 and object_in_lane3):
                    driveCar("Stop")
            else:
                driveCar("Go")
        else:
            driveCar("Go")

        key = cv2.waitKey(10) & 0xFF
        if key == ord('q'):     # kill command
            driveCar("Kill")
            break
        elif key == ord('w'):   # jump command
            driveCar("Jump")


cv2.destroyAllWindows()






