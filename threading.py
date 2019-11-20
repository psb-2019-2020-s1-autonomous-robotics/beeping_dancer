import logging
import threading
import time
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

motorB = Motor(Port.B)
sensor1 = UltrasonicSensor(Port.S1)
A = 440.000
G = 381.995
Fsharp = 369.994
E = 329.628
D = 293.665
C = 261.626
lowB = 246.942

songOver = False
danceOver = False

def sing(Hz = [G, G, Fsharp, Fsharp, lowB, D, lowB, lowB, G, G, Fsharp, Fsharp, lowB, 1, G, G, Fsharp, Fsharp, lowB, D, lowB, D, E, C, D, lowB, 1], d = [1, 1, 1, 1, 1, 0.5, 1.5, 1, 0.5, 1.5, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3]):
    #Sings the song entered. Default is Spooky Scary Skeletons
    logging.debug('Starting')
    for f in range(0,len(Hz)):
        if Hz[f] == 1:
            wait(250*d[f])
        else:
            brick.sound.beep(Hz[f], 250*d[f])
        wait(125)
    logging.debug('Exiting')


def dance():
    logging.debug('Starting')
    for a in range(0,4):
        motorB.run_target(500,360)
        motorB.run_target(500,0)
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

s = threading.Thread(name='sing', target=sing)
d = threading.Thread(name='dance', target=dance)

d.start()
t.start()
