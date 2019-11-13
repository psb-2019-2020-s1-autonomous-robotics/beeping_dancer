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

 

motorB = Motor(Port.B)

A = 440.000
G = 381.995
Fsharp = 369.994
E = 329.628
D = 293.665
C = 261.626
lowB = 246.942


Hz = [G, G, Fsharp, Fsharp, lowB, D, lowB, lowB, G, G, Fsharp, Fsharp, lowB, 1, G, G, Fsharp, Fsharp, lowB, D, lowB, D, E, C, D, lowB, 1]
d = [1, 1, 1, 1, 1, 0.5, 1.5, 1, 0.5, 1.5, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3]

for f in range(0,len(Hz)):
    if Hz[f] == 1:
        wait(250*d[f])
    else:
        brick.sound.beep(Hz[f], 250*d[f])
    motorB.run_target(20000, 50*f)
