import RPi.GPIO as gpio
from time import sleep

ledpin = (16, 20, 21)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
for pin in ledpin:
    gpio.setup(pin, gpio.OUT)
    
try:
    while True:
        for pin in ledpin:
            for i in range(2):
                gpio.output(pin, gpio.HIGH)
                sleep(1)
                gpio.output(pin, gpio.LOW)
                sleep(1)
                
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup() 