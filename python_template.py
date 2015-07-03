#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html

"""

import sys
from faker import Faker

# constants

gen = Faker()

# exception classes
# interface functions
# classes
# internal functions & classes

def main():
    print gen.paragraph()

if __name__ == '__main__':
    status = main()
    sys.exit(status)





''' 

Project Guidelines: 

- there is a good chance that I'll throw away all of this code. 
- The purpose of this file is to prototype out the basic functionality of this application in an efficient, pythonic, and readable manner.  
- Initially, the prototype will produce debugging output onto stdout
- When the prototype behaves as expected, I'll start wiring it to the 'Pi

****************************************************************

' {$STAMP BS2}
' {$PBASIC 2.5}

'deleted extra logic for proto board and light options

'**** ILLUSION CONSTANTS ****************************************************************
  'Sound            PIN 0   'Currently no solid state relay is mounted in this
                           ' position.
  Light_1  CON %0000000010 'The pins connected to the set of lights in mine shaft
  Light_2  CON %0000000100 'I don't use these light numbers but left them defined for clarity
  Light_3  CON %0000001000
  Light_4  CON %0000010000
  Light_5  CON %0000100000
  Light_6  CON %0001000000
  Light_7  CON %0010000000
  Light_8  CON %0100000000 'This is the light directly above the button

  Light_9  CON %1000000000 'This is also a normal gallery light.
  Pressed  CON  0          'Switch states
  Released CON  1
  Relay_Vibrater   PIN 10  'Operates a relay that controls power to the vibrator
                           ' located beneath the manskip
  Relay_RoomLight  PIN 11  'Transfer control of the room lights to this program.
                           ' and turns off the sodium vapor lights in the mine
                           ' shaft.
  'Spare          PIN 12   'Currently no solid state relay is mounted in this
                           ' position.
  Bell_Sounder     PIN 13  'Sounds the bell in the gallery
  'Spare            PIN 14  'Currently no solid state relay is mounted in this
                           ' position.
  StartSwitch      PIN 15  'The input pin is connected to the docent's "start"
                           ' switch. It is active-low
  '******************Frank added CONSTANTS for Proto Board ******************
  Bell_Sounder2    PIN 9   'Pizzo Speaker on proto Board, controls a light
                           'in the Illusion
'*************** Initial variables********
  Index1           VAR Byte      'Temporary storage of For-Next Index variables
  Index2           VAR Byte      'Temporary storage of For-Next Index variables
  InterblockTime   VAR Word      'The delay between passes through the strobe
                                 ' light sequence in milliseconds
  InterlightTime   VAR Word      'The time each strobe light is energized in
                                 ' milliseconds
  MinuteCount      VAR  Word     'Variable used to count loops which determine
                                 ' when one minute has passed waiting for the
                                 ' start button to be pressed
  Flag3            VAR  Bit      'Variable to determine if going back up
  UpDown           VAR  Bit      'Variabale used to determine if going up or down
                                 '1 is going down, 0 is going up

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


'********START STATE ***************************************************************

  StrtState:

      'Set the initial state.

      LOW Relay_RoomLight  'Turn on the mine-shaft lights and sodium vapor lights.

      GOSUB all            'Turn on all lights in the shaft

          SEROUT 0,$8054,["2"]  'Turns on general mining sounds.

'===============================================================================
'Now, wait (spin) until the docent's start switch is depressed.  While waiting
'mining noises will be played (sound track 2) looping automatically
'===============================================================================


       DO UNTIL (StartSwitch = Pressed ) 'LOOP UNTIL StartSwitch is pressed
         PAUSE 10
       LOOP

    Proceed:               'At this point, the start button has been pressed


         SEROUT 0,$8054,["S"]  'Fade out existing sound track.  This will quiet the mine sounds

'*******************************************************************************
'All sound has been turned off. Starting the Illusion'
'*******************************************************************************


    OUTS = (INS & %1111111011111110) 'Blink light over operators head
    PAUSE 500

    IF (StartSwitch = Released)  THEN continue3     'Don't wait any longer.  Let the ride begin
    PAUSE 500
    IF (StartSwitch = Released)  THEN continue3     'Don't wait any longer.  Let the ride begin
    PAUSE 1000
    IF (StartSwitch = Pressed)  THEN GOSUB IntroFeatures   'Button has been pressed over 2 seconds
                                                           'Play the introduction
    continue3:

    OUTS = (INS | %0000001111111110) 'Turn all lights back on

'*** Initial Bell Procedure (at start)***********************************************
'The following actions take place before the simulated ride starts down.
'Sound the BELL with the 3-3-2 sequence

    index2 = 3            'Ring bell 3 times
    GOSUB BellRing
    PAUSE 500
    GOSUB BellRing        'Ring bell another 3 times
    PAUSE 500
    index2 = 2            'ring bell twice more
    GOSUB BellRing

    'Turn off the normal ambient lighting circuit
     HIGH Relay_RoomLight

RETURN    'End of StrtState:



'******** ACCELERATION STATE PROCEDURE **********************************************

'This procedure controls the progressive activation of the lights used to simulate
'the forward movement of the man skip. These lights are referred to as strobe lights
'in this program due to the relatively short time they on on. At the start, the most
'distant light, #1, is illuminated. At about 15 feet #1 light is extinguished, and #2
'light is illuminated. The progression continues at 15 foot intervals until all lamps
'are extinguished.

AccelState:


    GOSUB one                 'Display first light
    PAUSE 2000                'Wait to simulate manskip acceleration

    HIGH Relay_Vibrater       'Start the Man Skip vibrator
    GOSUB two                 'Display second light
    PAUSE 1800

    SEROUT 0,$8054,["1"]  'Illusion Sounds

    GOSUB three               'Display third light
    PAUSE 1400

    GOSUB four                'Display 4th light
    PAUSE 1200

    GOSUB five                'Display 5th light
    PAUSE 1060

    GOSUB six                 'Display 6th light
    PAUSE 950

    GOSUB seven             'Turn on 7th light if No7 = 0
    PAUSE 900

    GOSUB NoLights

RETURN  'The end of the routine that accelerates the Illusion down the shaft

'************************************************************************************
'******** CONSTANT SPEED STATE PROCEDURE ******************************************
'***********************************************************************************

ConstSpeedState:

  'This procedure is similar to the AccelState procedure, but, due to the constant
  'speed the time between switching the lights is constant, thus a more compact coding
  'is feasible.
  'This routine will work for both up and down movement controlled by UpDown variable


   InterblockTime = 2000         'Delay time in milliseconds before simulating
                                        'passage through the next sequence of mine
                                        'shaft strobe lights
   InterlightTime = 625          'Time in milliseconds between switching the
                                        'strobe lights
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 439
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 291
   GOSUB ExecLights


   InterblockTime = 1000
   InterlightTime = 229
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 271
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 395
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 189
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 354
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 188
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 354
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 375
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 186
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 186
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 355
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 229
   GOSUB ExecLights

   InterblockTime = 1000
   InterlightTime = 300
   GOSUB ExecLights

   InterblockTime = 1500
   InterlightTime = 400
   GOSUB ExecLights

   InterblockTime = 1500
   InterlightTime = 500
   GOSUB ExecLights

RETURN   'End of constant speed state

'************************************************************************************
ExecLights:

  PAUSE InterblockTime

  IF UpDown = 1 THEN      'Going down if UpDown was set to 1

    ' Now step through switching on and off the 9 mine shaft lights creating the
    ' stroboscopic illusion that the manskip is moving down the shaft.

      GOSUB one
      PAUSE  InterlightTime            'Wait the defined on/off time
      GOSUB Two
      PAUSE  InterlightTime
      GOSUB three
      PAUSE  InterlightTime
      GOSUB four
      PAUSE  InterlightTime
      GOSUB five
      PAUSE  InterlightTime
      GOSUB six
      PAUSE  InterlightTime
      GOSUB seven
      PAUSE  InterlightTime

   ELSE  'Going up if UpDown was set to 0

   ' Now step through switching on and off the 9 mine shaft lights creating the
    ' stroboscopic illusion that the manskip is moving up the shaft.
      GOSUB seven
      PAUSE  InterlightTime

      GOSUB Six
      PAUSE  InterlightTime

      GOSUB Five
      PAUSE  InterlightTime

      GOSUB Four
      PAUSE  InterlightTime

      GOSUB Three
      PAUSE  InterlightTime

      GOSUB Two
      PAUSE  InterlightTime

      GOSUB One
      PAUSE  InterlightTime

   ENDIF

      GOSUB NoLights

RETURN   'end of routine that flashes the lights sequencely up the mine

'************************************************************************************
'******** DECELERATION STATE PROCEDURE **********************************************

'The actions of this procedure can be considered the complement of those in the
'Acceleration State Procedure. Speed of the simulated manskip is diminished to zero;
'light #7 is left illuminate; the sound is terminated, as is the vibrator.

DecelState:
  PAUSE 500

  GOSUB One
  PAUSE 770                   'Increasing wait time simulating deceleration

  GOSUB Two
  PAUSE 820

  GOSUB Three
  PAUSE 880

  GOSUB Four
  PAUSE 950

  GOSUB Five
  PAUSE 1060

  GOSUB Six
  PAUSE 1200

  GOSUB Seven
  PAUSE 1400

  LOW Relay_Vibrater          'Stop the Man Skip vibrator

  SEROUT 0,$8054,["S"]  'Fade out existing sound track.

  PAUSE 1800

  GOSUB NoLights

RETURN   'End of deceleration state

'************************************************************************************
'*** STOP STATE PROCEDURE ***********************************************************
'The following actions take place after the simulated ride has come to a stop.
StpState:

  'Sound the bell and turn on Light #7 to inform the docent-operator the dynamic
  'aspect of the simulation has concluded. The docent may react with the audience
  'at this time when the noise of the simulation has subsided and the illumination
  'remains DIM.  When the stop button is again pressed all lights will turn on and
  'the background sounds will start.  Optionally,if the docent holds the button down
  'for more than 1 full second, the ride will go back up before turning the lights on.

  GOSUB Eight       'Turn on the lamp at the docent's station

  index2 = 1        'Ring bell once
  GOSUB BellRing


  'Now, wait (spin) until the docent's start switch is depressed.  If depressed
  'for more than 2 seconds the man skiff will go back up.  I check the switch
  'after 1 second and immediately quit if the switch has been released instead
  'of waiting the full 2 seconds
    Flag3 = 0                             'Use to decide if we travel back up
    continue0:
    IF (StartSwitch = Released ) THEN continue0   'Waiting for button press

    'Blink light 8
    GOSUB NoLights
    PAUSE 500
    GOSUB eight
    IF (StartSwitch = Released)  THEN continue1   'Don't wait any longer
    PAUSE 500
    IF (StartSwitch = Released)  THEN continue1   'Don't wait any longer
    PAUSE 1000
    GOSUB NoLights  'Turn light back off and start up ride
    IF (StartSwitch = Pressed)  THEN Flag3 = 1   'Button has been pressed over 2 seconds
                                          'so man skiff will go back up
    continue1:

RETURN  'End of routine that puts the Illusion in the STOP state

'************************************************************************************
UpStart:  'The ride will accelerate in the up direction


'     Sound the bell with the 3-3-1 sequence (Up with caution)

    index2 = 3            'Ring bell 3 times
    GOSUB BellRing
    PAUSE 500
    GOSUB BellRing        'Ring bell another 3 times
    PAUSE 500
    index2 = 1            'ring bell once more
    GOSUB BellRing

     GOSUB eight          'Turn on light 8.  This is ignoring the No8 flag
     PAUSE 1800

     HIGH Relay_Vibrater

     SEROUT 0,$8054,["1"] 'Illusion Sounds for ride up

     GOSUB seven
     PAUSE 1400

     GOSUB six
     PAUSE 1200

     GOSUB five
     PAUSE 1060

     GOSUB four
     PAUSE 950

     GOSUB three
     PAUSE 880

     GOSUB two
     PAUSE 820

     GOSUB one
     PAUSE 770

RETURN 'End of the routine accelerating the the ride up

'**********************************************************************************
UpDecel:

     GOSUB seven
     PAUSE 820

     GOSUB six
     PAUSE 880

     GOSUB five
     PAUSE 950

     GOSUB four
     PAUSE 1060

     GOSUB three
     PAUSE 1200

     GOSUB two
     PAUSE 1400

     SEROUT 0,$8054,["S"] 'Fade out the sound

     GOSUB one
     PAUSE 800

     LOW relay_Vibrater

     index2 = 1            'ring bell
     GOSUB BellRing

RETURN   'End of the up deceleration

'**********************************************************************************
'Rings the bell on the Illusion
'**********************************************************************************
BellRing:

  FOR index1 = 1 TO index2
    HIGH Bell_Sounder         'Turn on the Bell circuit
    PAUSE 375                 'Bell duration
    LOW Bell_Sounder          'Turn off the bell
    PAUSE 125
  NEXT


RETURN

'*********************************************************************************
'***********IntroFeatures introduces the Illusion features in a less scary mode **
'*********************************************************************************

IntroFeatures:

  OUTS = (INS | %0000001111111110) 'Turn all lights back on

  SEROUT 0,$8054,["4"] 'Play Introduction sound track


  PAUSE 25000

  UpDown = 1                 'Strobe the lights once up the shaft
  InterblockTime = 900
  InterlightTime = 900
  GOSUB ExecLights

  InterblockTime = 700      'once more faster
  InterlightTime = 700
  GOSUB ExecLights

  HIGH Relay_Vibrater

  InterblockTime = 500      'once more faster
  InterlightTime = 500
  GOSUB ExecLights

  LOW  Relay_Vibrater

  PAUSE 16000

  SEROUT 0,$8054,["S"] 'Fade out the sound


  GOSUB all                  'Turn on all the lights in the shaft

  PAUSE 2000

RETURN


'**********************************************************************************
one:         'Read the 16 pin states, use the AND function to turn off all 9
             'LED's then use the OR function to turn on Light 1
    OUTS = (INS & %1111110000000001) | Light_1  ' Turns on Light 1

RETURN

'**********************************************************************************
two:

    OUTS = (INS & %1111110000000001) | Light_2 'Turns on light 2

RETURN

'**********************************************************************************
three:
    OUTS = (INS & %1111110000000001) | Light_3 'Turns on light 3

RETURN

'**********************************************************************************
four:
    OUTS = (INS & %1111110000000001) | Light_4 'Turns on Light 4

RETURN

'**********************************************************************************
five:

    OUTS = (INS & %1111110000000001) | Light_5 'Turns on Light 5

RETURN

'**********************************************************************************
six:

    OUTS = (INS & %1111110000000001) | Light_6 'Turns on light 6

RETURN

'**********************************************************************************
seven:

    OUTS = (INS & %1111110000000001) | Light_7 'Turns on light 7

RETURN

'**********************************************************************************
eight:

    OUTS = (INS & %1111110000000001) | Light_8 'Turns on light 8

RETURN

'**********************************************************************************
nine:

    OUTS = (INS & %1111110000000001) | Light_9 'Turns on light 9

RETURN

'**********************************************************************************
all:

    OUTS = (INS | %0000001111111110)          'Turns on all 9 lights

RETURN

'**********************************************************************************
NoLights:

    OUTS = (INS & %1111110000000001)       'Turns off all lights

RETURN
'**********************************************************************************
ServiceWait:

PAUSE 2000
 DO UNTIL (StartSwitch = Pressed ) 'LOOP UNTIL StartSwitch is pressed
 LOOP
RETURN

'**********************************************************************************
'************************************************************************************

'''