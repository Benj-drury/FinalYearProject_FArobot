#Drive Code - Version 3 - function

import time
import FA

# initialize FA 
fa = FA.Create()


def driveCar(drive_mode):
    """
    This function controls the car based on the provided drive_mode.

    Args:
        drive_mode: A string specifying the desired driving mode.
        - "Go": Drives the car forward while adjusting direction based on sensor readings.
        - "Jump": Makes the car perform a jump (backward then forward motion).
        - "Setup": Initializes the car, including setting up communication, motors, and playing a jingle.
        - "Kill": Stops the car, plays a reversed jingle, closes communication, and exits the program.
        - "LeftPath": Follows a pre-defined left path trajectory.
        - "RightPath": Follows a pre-defined right path trajectory.
        - "Stop": Stops the car
    """

    white = 50  # threshold value for white line sensor readings
    TravelDistance = 22  # motor travel distance
    turnCorrection = 10  # motor speed for turns

    jingle_notes = [  # musical notes for the jingle played during setup
        (523, 50), (587, 50), (659, 50), (698, 50), (783, 50),
        (880, 50), (987, 50), (1046, 100)
    ]

    if drive_mode == "Go":
        left_sensor = fa.ReadLine(0)  # read left line sensor value
        right_sensor = fa.ReadLine(1)  # read right line sensor value

        # check sensor readings and adjust direction accordingly
        if left_sensor >= white and right_sensor <= white:
            print('Go Right,')
            print('left sensor =', left_sensor, 'right sensor =', right_sensor)
            fa.SetMotors(turnCorrection, -turnCorrection)  # turn right
        elif right_sensor >= white and left_sensor <= white:
            print('Go Left,')
            print('left sensor =', left_sensor, 'right sensor =', right_sensor)
            fa.SetMotors(-turnCorrection, turnCorrection)  # turn left
        elif right_sensor > white and left_sensor > white:
            print('Go Back,')
            print('left sensor =', left_sensor, 'right sensor =', right_sensor)
            fa.Backwards(TravelDistance * 2)  # move backward to correct
            fa.Left(TravelDistance)  # turn slightly left
        else:
            print('Go Straight,')
            print('left sensor =', left_sensor, 'right sensor =', right_sensor)
            fa.Forwards(TravelDistance * 2) # move forward straight

    elif drive_mode == "Jump":
        fa.Backwards(TravelDistance)  # move backward
        fa.Forwards(TravelDistance)  # move forward (jump)

    elif drive_mode == "Setup":
        MESSAGE1 = "Car Setup initiated"
        MESSAGE2 = "GO!"
        comport = 5

        print(MESSAGE1)
        fa.ComOpen(comport)  # open communication port
        fa.SetMotors(0, 0)  # stop motors
        fa.LCDClear()  # clear LCD display
        fa.LCDPrint(30, 10, MESSAGE1)  # print setup message on LCD
        fa.LCDBacklight(50)  # pet LCD backlight

        # play jingle notes with a slight delay between each
        for note, length in jingle_notes:
            fa.PlayNote(note, length)
            time.sleep(length / 1000)

        fa.LCDClear()
        fa.LCDPrint(30, 10, MESSAGE2)  # print "GO!" message on LCD
        fa.LCDBacklight(0)  # turn off LCD backlight
        print("\nsetup complete")

    elif drive_mode == "Kill":
        fa.SetMotors(0, 0)  # stop motors
        # play jingle notes in reverse order
        for note, length in reversed(jingle_notes):
            fa.PlayNote(note, length)

        fa.ComClose()  # close communication port
        print("\n\n\n-------KILLED-------\n\n\n")

    elif drive_mode == "LeftPath":
        fa.Left(45)
        fa.Forwards(130)
        fa.Right(45)
        fa.Forwards(20)
        
    elif drive_mode == "RightPath":
        fa.Right(55)
        fa.Forwards(85)
        fa.Left(55)

    elif drive_mode == "Stop":
        print("\n\n\n-------STOP-------\n\n\n")
        fa.SetMotors(0,0)

       




