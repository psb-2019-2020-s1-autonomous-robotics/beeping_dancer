#!/usr/bin/env pybricks-micropython
#https://en.wikipedia.org/wiki/Piano_key_frequencies
#https://www.musicnotes.com/images/productimages/large/mtd/MN0168952.gif
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
 
# Write your program here
motorB = Motor(Port.B)
sensor1 = UltrasonicSensor(Port.S1)
A = 440.000
G = 381.995
Fsharp = 369.994
D = 293.665
C = 261.626
lowB = 246.942

#Hz = [261.626, 261.626, 391.995, 391.995, 440.000, 440.000, 391.995], d = [500, 500, 500, 500, 500, 500, 1000]

def sing(Hz = [G, G, Fsharp, Fsharp, lowB, D, lowB, lowB, G, G, Fsharp, Fsharp], d = [500, 500, 500, 500, 500, 250, 750, 500, 250, 750, 500, 500, 500]):
 
    for f in range(0,len(Hz)):
        brick.sound.beep(Hz[f], 0.5*d[f])
        wait(125)
sing()
#while True:
    #if sensor1.distance() < 1000:
        #brick.sound.beep()
        #for a in range(0,4):
            #motorB.run_target(500,360)
            #motorB.run_target(500,0)

       # break
