#!/usr/bin/env python

from time import sleep

Light = []
Light[1] = '%0000000010' #'The pins connected to the set of lights in mine shaft
Light[2] = '%0000000100' #'I don't use these light numbers but left them defined for clarity
Light[3] = '%0000001000'
Light[4] = '%0000010000'
Light[5] = '%0000100000'
Light[6] = '%0001000000'
Light[7] = '%0010000000'
Light[8] = '%0100000000' #'This is the light directly above the button
Light[9] = '%1000000000' # 'This is also a normal gallery light.

PIN = {}
PIN[0] = 'Sound' #'Currently no solid state relay is mounted in this position.
PIN[10] = 'Relay_Vibrator' #'Operates a relay that controls power to the vibrator located beneath the manskip
PIN[11] = 'Relay_RoomLight' #'Transfer control of the room lights to this program. and turns off the sodium vapor lights in the mine shaft.
PIN[14] = 'Spare' # TODO: delete this one? 'Currently no solid state relay is mounted in this position.
PIN[15] = 'StartSwitch' #'The input pin is connected to the docent's "start" switch. It is active-low
PIN[9] = 'Bell_Sounder2' #
PIN[13] = 'Bell_Sounder' #'Sounds the bell in the gallery
PIN[11] = 'Relay_RoomLight' #
PIN[12] = 'Spare' # TODO: delete this one?


def olros_presentation(var):
    print 'olros_presentation: ' + var

def lights(var1, var2):
    print 'lights: ' + var1 + var2

def sound(var):
    print 'sound: ' + var

def StartSwitch(var):
    print var

def relay_vibrator(var):
    print 'relay_vibrator: ' + var

def ServiceLoop():
    lights('shaft-all', 'on')
    lights('sodium-vapor', 'on')
    relay_vibrator('man skip')
    relay_vibrator('under man skip')
    lights('room', 'off')
    lights(1, 'on')
    sleep 1
    lights(2, 'on')
    sleep 1
    lights(3, 'on')
    sleep 1
    lights(4, 'on'
    sleep 1
    lights(5, 'on')
    sleep 1
    lights(6, 'on')
    sleep 1
    lights(7, 'on')
    sleep 1
    lights(8, 'on')
    sleep 1
    lights(9, 'on')
    sleep 1
    lights('all', 'off')

# Main

while True: # loop forever
    lights('mineshaft room', 'on') #'Set the initial state.
    lights('sodium-vapor', 'on')
    lights('shaft-all', 'on')
    sound('general mining sounds')

    while StartSwitch(1) == 1: # when StartSwitch is pressed, begin loop
        sleep 5 # wait 5 seconds
        if StartSwitch(0) == 1: # enter service loop if user is still pressing the button
            ServiceLoop()
        else: # enter presentation loop
            olros_presentation('intro')
            lights('mineshaft', 'on')
            lights('sodium-vapor', 'on') # TODO: lights('on')?
            lights('shaft-all', 'on')
            sound('off')
            olros_presentation('mine')



'''


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
