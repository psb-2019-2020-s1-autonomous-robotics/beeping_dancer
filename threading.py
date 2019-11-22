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
import threading

motorB = Motor(Port.B)
sensor1 = UltrasonicSensor(Port.S1)
A = 440.000
G = 381.995
Fsharp = 369.994
E = 329.628
D = 293.665
C = 261.626
lowB = 246.942

hertz = [G, G, Fsharp, Fsharp, lowB, D, lowB, lowB, G, G, Fsharp, Fsharp, lowB, 1, G, G, Fsharp, Fsharp, lowB, D, lowB, D, E, C, D, lowB, 1]
duration = [1, 1, 1, 1, 1, 0.5, 1.5, 1, 0.5, 1.5, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3]
song_over = 1 
dance_over = 1
def sing():
    #Sings the song entered. Default is Spooky Scary Skeletons
    for f in range(0,len(hertz)):
        if hertz[f] == 1:
            wait(250*duration[f])
        else:
            brick.sound.beep(hertz[f], 250*duration[f])
        wait(125)
    song_over = 0

def dance():
    
    for a in range(0,4):
        motorB.run_target(500,360)
        motorB.run_target(500,0)
    dance_over = 0

s = threading.Thread(name='sing', target=sing)
d = threading.Thread(name='dance', target=dance)

d.start()
print("something")
s.start()

while song_over or dance_over:
    print(song_over, dance_over)
