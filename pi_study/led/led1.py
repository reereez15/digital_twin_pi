import RPi.GPIO as gpio
from time import sleep

ledpin = (16, 20, 21)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(ledpin, gpio.OUT)

try:
    while True:
        number = int(input("led number(1/2/3)"))
        mode = input("mode(on/off): ")
        
        if mode == "on":
            gpio.output(ledpin[number - 1], gpio.HIGH)
        elif mode == "off":
            gpio.output(ledpin[number - 1], gpio.LOW)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup() 