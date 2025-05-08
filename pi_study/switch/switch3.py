import RPi.GPIO as gpio
from time import sleep

class led:
    def __init__(self, pin, color):
        self.pin = pin
        self.color = color
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, gpio.LOW) 
        
    def blink(self, count):
        for _ in range(count):
            gpio.output(pin, gpio.HIGH)
            sleep(time)
            gpio.output(pin, gpio.LOW)
            sleep(time)
            
    def ledOn(self):
        gpio.output(self.pin, gpio.HIGH)
        
    def ledOff(self):
        gpio.output(self.pin, gpio.LOW)

class Button:
    def __init__(self, pin, setOnPressed):
        self.pin = pin
        self.prevState = gpio.LOW
        self.onPressed = setOnPressed
        gpio.setup(self.Pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        
    def waitPressed(self):
        currentState = gpio.input(self.pin)
        if self.checkPressed(currentState):
            self.onPressed()
        self.prevState = currentState
        sleep(0.05)
        
    def checkPressed(self, currentState):
        return currentState == gpio.HIGH and self.prevState == gpio.LOW

def open():
    print("open")

def close():
    print("close")

leds = (led(16, ""), led(21, ""))            
buttons = (Button(13), Button(6))

try:
    while True:
        for button in buttons:
            button.waitPressed()

except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()