#!/usr/bin/env python

import sys
import random
from time import sleep
# import RPI.GPIO as GPIO


def light(input):           # The pins connected to the set of lights in mine shaft
    if input == 1:
        print('Light level 1 - GPIO %0000000010')
    elif input == 2:
        print('Light level 2 - GPIO %0000000100')
    elif input == 3:
        print('Light level 3 - GPIO %0000001000')
    elif input == 3:
        print('Light level 4 - GPIO %0000010000')
    elif input == 4:
        print('Light level 5 - GPIO %0000100000')
    elif input == 5:
        print('Light level 6 - GPIO %0001000000')
    elif input == 6:
        print('Light level 7 - GPIO %0010000000')
    elif input == 7:
        print('Light level 8 - GPIO %0100000000')    # This is the light directly above the button
    elif input == 8:
        print('Light level 9 - GPIO %1000000000')
    else:
        print('ERROR')


def pin(input):
    if input == 1:
        print("Relay_Vibrator GPIO %0000000000")
    elif input == 2:
        print("Relay_Roomlight GPIO %0000000000")
    elif input == 3:
        print("Spare GPIO %0000000000")
    elif input == 4:
        print("Bell_Sounder GPIO %0000000000")
    elif input == 5:
        print("Spare GPIO %0000000000")
    elif input == 6:
        print("StartSwitch GPIO %0000000000")
    elif input == 6:
        print("Bell_Sounder2 GPIO %0000000000")
    else:
        print('ERROR')


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
    print('play_mining_sounds()') # plays mining sounds until the button is pressed


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


def return_ride():
    print ('return ride')


### main ###

while True:
    initialize()
    set_initial_state()
    start_sequence()
    sleep(1)
    fade_sounds()
    light_sequence()
    sleep(1)
    return_ride()
    sleep(1)
    end_sequence()
