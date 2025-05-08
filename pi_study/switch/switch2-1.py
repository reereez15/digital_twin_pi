import RPi.GPIO as gpio
from time import sleep

swPin = (6, 13)

gpio.setmode(gpio.BCM)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

prevState = gpio.LOW
prevState1 = gpio.LOW
try:
    while True:
        swState = gpio.input(swPin[0])
        if swState == gpio.HIGH and prevState == gpio.LOW:
            print(1)
        prevState = swState
        sleep(0.05)
        
        swState2 = gpio.input(swPin[1])
        if swState2 == gpio.HIGH and prevState1 == gpio.LOW:
            print(1)
        prevState1 = swState2
        sleep(0.05)
        
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()