#!/usr/bin/env python

from time import sleep

def olros_presentation(var):
    print 'olros_presentation: ' + var

def lights(var1, var2):
    print 'lights: ' + var1 + var2

def sound(var):
    print 'sound: ' + var

def StartSwitch(var):
    if var == 1:
        print 'StartSwitch: pressed'
        return var
    else:
        print 'StartSwitch: released'
        return var

def relay_vibrator(var):
    print 'relay_vibrator: ' + var

def ServiceLoop():
    lights('shaft-all', 'on')
    lights('sodium-vapor', 'on')
    relay_vibrator('man skip')
    relay_vibrator('under man skip')
    lights('room', 'off')
    lights(1, 'on')
    sleep(1)
    lights(2, 'on')
    sleep(1)
    lights(3, 'on')
    sleep(1)
    lights(4, 'on')
    sleep(1)
    lights(5, 'on')
    sleep(1)
    lights(6, 'on')
    sleep(1)
    lights(7, 'on')
    sleep(1)
    lights(8, 'on')
    sleep(1)
    lights(9, 'on')
    sleep(1)
    lights('all', 'off')

# Main

while True: # loop forever
    print('\n\n------ BEGIN LOOP ------\n\n')
    lights('mineshaft room', 'on') #'Set the initial state.
    lights('sodium-vapor', 'on')
    lights('shaft-all', 'on')
    sound('general mining sounds')

    while StartSwitch(1) == 1: # when StartSwitch is pressed, begin loop
        sleep(5) # wait 5 seconds
        if StartSwitch(0) == 1: # enter service loop if user is still pressing the button
            ServiceLoop()
        else: # enter presentation loop
            olros_presentation('intro')
            lights('mineshaft', 'on')
            lights('sodium-vapor', 'on') # TODO: lights('on')?
            lights('shaft-all', 'on')
            sound('off')
            olros_presentation('mine')
