#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
import sys
import random
import time
# from faker import Faker
# import RPI.GPIO as GPIO


# I put the lights into an array, mostly to show you how to handle arrays in python
# You can call elements from an array by number, like this:
# print(LIGHT[2]) # <- this will print out the second light

LIGHT = []
LIGHT.append("%0000000010")  # The pins connected to the set of lights in mine shaft
LIGHT.append("%0000000100")  # I don't use these light numbers but left them defined for clarity
LIGHT.append("%0000001000")
LIGHT.append("%0000010000")
LIGHT.append("%0000100000")
LIGHT.append("%0001000000")
LIGHT.append("%0010000000")
LIGHT.append("%0100000000")  # This is the light directly above the button
LIGHT.append("%1000000000")
BUTTONPRESSED = 0
BUTTONRELEASED = 1

# Likewise with the PINS - I put them in a dictionary
# You call dictionary elements by key name:
# print(PIN["Relay_Vibrator"])

PIN = {}
PIN[10] = "Relay_Vibrator"
PIN[11] = "Relay_Roomlight"
PIN[12] = "Spare"
PIN[12] = "Bell_Sounder"
PIN[13] = "Spare"
PIN[14] = "StartSwitch"
PIN[15] = "Bell_Sounder2"


def set_initial_state():
    print("\nset initial state: StrtState")
    turnOnMineshaftLights()
    turnOnAllLights()
    playMiningSounds()
    while StartSwitchPressed == 0: # plays mining sounds until the button is pressed
        sleep(1)
    fadeSounds()


def start_sequence():
  print("\nstart sequence")


def end_sequence():
  print("\nend sequence")
  
  
def print_lights():
    print("\nprint lights")
    loops = 1
    for i in LIGHT:
        print ("LIGHT{}: {}".format(loops, i))
        loops += 1


def print_pins():
    for x in PIN:
        print("PIN{} {}".format(x, PIN[x]))


def start_tunnel_ride():
  print("\nstart runnel ride")

  
def return_tunnel_ride():
  print("\nreturn tunnel ride")
  
  
def play_orlos_presentation():
  print("\nplay orlos presentation")


def turn_on_mine_shaft_lights():
    print("Mineshaft Lights = ON # LOW Relay_RoomLight")


def turn_on_all_lights():
    print("All Lights = ON")


def turn_on_mining_sounds():
    print("Mining sounds = ON")


def fade_sounds():
    print("All sounds fade out now")


def blink_light_over_operator():
    print("Blink Lights over the operator's head")
    sleep(1)


def accel_state():
    displayFirstLight()
    sleep(2) # Wait to simulate manskip acceleration
    startManSkipVibrator()
    displaySecondLight()
    sleep(1)
    playIllusionSounds()
    displayThirdLight()
    sleep(1)
    displayFourthLight()
    sleep(1)
    displayFifthLight()
    sleep(1)
    displaySixthLight()
    sleep(1)
    displaySeventhLight()



### main ###

def main():
    set_initial_state()
    start_sequence()
    time.sleep(1)

    buttonPressed = 0
    if buttonPressed == 1:
        print("You pressed the button")
    else:
        play_orlos_presentation()
    start_tunnel_ride()
    time.sleep(1)
    print_lights()
    time.sleep(1)
    return_tunnel_ride()
    end_sequence()


if __name__ == '__main__':
    status = main()
    sys.exit(status)


'''
'**** MAIN PROGRAM *****************************************************************

Main:
    'Set the pin I/O directions and Initialize

      OUTS = %0000000000000000       'Initialize ports to off default is 0 anyway

      DIRS = %0111111111111111       'The only input pin is bit 15.  7FFF hex

      PAUSE 250 'Give the sound card time to initialize

          IF (StartSwitch = Pressed )   THEN 'Just play Orlos presentation if StartSwitch
                                         'is pressed during reset

           LOW Relay_RoomLight  'Turn on the mine-shaft lights and sodium vapor lights.

           GOSUB all            'Turn on all lights in the shaft
           DO

              SEROUT 0,$8054,["S"]     'Stop all sound

              PAUSE 2000

              SEROUT 0,$8054,["3"]  'Start Olro Presentation in the mine

              PAUSE 3000

               ServiceLoop:

                IF (StartSwitch = Released ) THEN
                PAUSE 100
                GOTO ServiceLoop  'Watch for start switch being pressed
                ENDIF
                PAUSE 5000
                IF (StartSwitch = Released  ) THEN
                GOTO ServiceLoop  'Start service mode if switch pressed for 5+ seconds
                ENDIF
                   DO
                      SEROUT 0,$8054,["S"]

                      GOSUB all     ' turn on all shaft lights
                      LOW Relay_RoomLight  'Turn on the mine-shaft lights and sodium vapor lights.
                      HIGH Relay_Vibrater  'Start the Man Skip vibrator
                      GOSUB ServiceWait
                      LOW Relay_Vibrater   'Turn off vibrator under man skip
                      GOSUB ServiceWait
                      HIGH Relay_RoomLight 'Turn off room lights
                      GOSUB one   'Turn lights on one at a time then wait for button press
                      GOSUB ServiceWait
                      GOSUB two
                      GOSUB ServiceWait
                      GOSUB three
                      GOSUB ServiceWait
                      GOSUB four
                      GOSUB ServiceWait
                      GOSUB five
                      GOSUB ServiceWait
                      GOSUB six
                      GOSUB ServiceWait
                      GOSUB seven
                      GOSUB ServiceWait
                      GOSUB eight
                      GOSUB ServiceWait
                      GOSUB nine
                      GOSUB ServiceWait
                      GOSUB all
                      GOSUB ServiceWait
                   LOOP
           LOOP
      ENDIF

      'If we get past here, the StartStop switch was not pressed during the last reset

          SEROUT 0,$8054,["S"]  'STOP all sound

          PAUSE 1000

        'Start periodic processing.
      DO
            GOSUB StrtState
            GOSUB AccelState
            UpDown = 1
            GOSUB ConstSpeedState
            GOSUB DecelState
            GOSUB StpState
            IF Flag3 = 0 THEN continue5 'The Illusion is not going back up if Flag3 = 0
                                        'Flag3 is set in the previous StpState by how long
                                        'the Start Button is depressed.
            GOSUB  UpStart
            UpDown = 0
            GOSUB  ConstSpeedState
            GOSUB  UpDecel
            continue5:
            GOSUB eight         'Turn on lights slowly
            PAUSE 1000
            GOSUB all
            PAUSE 1000
      LOOP            'End of the program loop
  END                 'End of the Main program
'************************************************************************************
'''