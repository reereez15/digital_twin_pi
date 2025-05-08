import RPi.GPIO as gpio
from time import sleep

ledpin = (16, 20, 21)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
for pin in ledpin:
    gpio.setup(pin, gpio.OUT)

try:
    isOnAll = False
    while True:
        for pin in ledpin:
            if isOnAll:
                gpio.output(pin, gpio.LOW)
            else:
                gpio.output(pin, gpio.HIGH)
            sleep(0.1)
        isOnAll = not isOnAll
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup() 