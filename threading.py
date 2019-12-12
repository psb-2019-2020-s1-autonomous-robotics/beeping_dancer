#!/usr/bin/env pybricks-micropython
 
'''
BEEPING DANCER

To run, put your hand in front of the sensor. The ultrasonic distance sensor causes the program to dance and beep “Spooky Scary Skeletons” when it senses a nearby object. The frame is a large piece of cardboard with the cardboard limbs and head stuck on the front. On the other side is a system of gears connected to the limbs and the motor that causes the limbs to swivel back and forth. 

 
This robot was made by Vivi Wickersham and Maya Smith in their Autonomous Robotics class using the following links:
https://en.wikipedia.org/wiki/Piano_key_frequencies
https://www.musicnotes.com/images/productimages/large/mtd/MN0168952.gif
https://pymotw.com/3/threading/
'''
 
#These import the necessary modules
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import threading
 
 
#This defines the motor and sensor
motorB = Motor(Port.B)
sensor1 = UltrasonicSensor(Port.S1)
 
 
#This tells the robot to play an A at 400.000 Hertz, a G at 381.995, and so on
A = 440.000
G = 381.995
Fsharp = 369.994
E = 329.628
D = 293.665
C = 261.626
lowB = 246.942
 
 
#This saves the song "Spooky Scary Skeletons" into two variables: hertz and duration
hertz = [G, G, Fsharp, Fsharp, lowB, D, lowB, lowB, G, G, Fsharp, Fsharp, lowB, 1, G, G, Fsharp, Fsharp, lowB, D, lowB, D, E, C, D, lowB, 1]
duration = [1, 1, 1, 1, 1, 0.5, 1.5, 1, 0.5, 1.5, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3]
 
 
song_on = True
dance_on = True
 
 
def sing():
   '''This function plays "Spooky Scary Skeletons" when called. At the end, it tells the whole program that the song in over.'''
   for f in range(0,len(hertz)):
       if hertz[f] == 1:
           wait(250*duration[f])
       else:
           brick.sound.beep(hertz[f], 250*duration[f])
       wait(125)
   global song_on
   song_on = False
 
 
 
 
def dance():
   '''This function makes the robot dance. At the end, it tells the whole program that the dance in over.'''
   for a in range(0,4):
       motorB.run_target(500,360)
       motorB.run_target(500,0)
   global dance_on
   dance_on = False
 
 
#Threading is a python module with which one can run multiple programs at the same time. This sets threading up. "s" will run sing and "d" will run dance.
s = threading.Thread(name='sing', target=sing)
d = threading.Thread(name='dance', target=dance)
 
 
#This part actually runs the code if something is detected within half a meter.
while True:
   if sensor1.distance() < 500:
       song_on = True
       dance_on = True
       d.start()
       s.start()
 
 
       while song_on or dance_on:
           pass
