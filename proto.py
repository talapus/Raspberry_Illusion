#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
import sys
import random
from time import sleep

# import RPI.GPIO as GPIO


BUTTONPRESSED = 0
BUTTONRELEASED = 1


def light(input):           # The pins connected to the set of lights in mine shaft
    if input == 1:
        print('GPIO %0000000010')
    elif input == 2:
        print('GPIO %0000000100')
    elif input == 3:
        print('GPIO %0000001000')
    elif input == 3:
        print('GPIO %0000010000')
    elif input == 4:
        print('GPIO %0000100000')
    elif input == 5:
        print('GPIO %0001000000')
    elif input == 6:
        print('GPIO %0010000000')
    elif input == 7:
        print('GPIO %0100000000')    # This is the light directly above the button
    elif input == 8:
        print('GPIO %1000000000')
    else:
        pass


def pin(input):
    if input == 1:
        PIN.append("Relay_Vibrator")
    elif input == 2:
        PIN.append("Relay_Roomlight")
    elif input == 3:
        PIN.append("Spare")
    elif input == 4:
        PIN.append("Bell_Sounder")
    elif input == 5:
        PIN.append("Spare")
    elif input == 6:
        PIN.append("StartSwitch")
    elif input == 6:
        PIN.append("Bell_Sounder2")
    else:
        print


def start_sequence():
  print("\nstart sequence")


def end_sequence():
  print("\nend sequence")


def light_sequence():
    print("\nprint lights")
    for i in range(0,9):
        print ("LIGHT{}: {}".format(i, light(i)))


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


def ambient_tunnel_noise():
    print("*Ambient tunnel noise playing*")


def blink_light_over_operator():
    print("Blink Lights over the operator's head")
    sleep(1)





def set_initial_state():
    print('turn_On_mineshaft_lights()')
    print('turn_on_all_lights()')
    print('play_mining_sounds()')
    while StartSwitchPressed == 0: # plays mining sounds until the button is pressed
        sleep(1)
        play_mining_sounds()
    fadeSounds()


def initialize():
    print("OUTS = '%0000000000000000'")  #'Initialize ports to off default is 0 anyway
    print("DIRS = '%0111111111111111'")  #'The only input pin is bit 15.  7FFF hex
    sleep(2.5) # 'Give the sound card time to initialize


def vibrator(input):
    if input == 'on':
        print('Manskip Vibrator: ON')
    elif input == 'off':
        print('Manskip Vibrator: OFF')
    else:
        print('ERROR: please specify ON or OFF')

### main ###


while True:
    initialize()
    set_initial_state()
    start_sequence()
    sleep(1)
    light_sequence()
    sleep(1)
    return_ride()
    sleep(1)
    end_sequence()

'''
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


################################################################################################


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
