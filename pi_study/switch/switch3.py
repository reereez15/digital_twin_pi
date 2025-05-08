import RPi.GPIO as gpio
from time import sleep
from threading import Thread

class led:
    def __init__(self, pin, color):
        self.pin = pin
        self.color = color
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, gpio.LOW) 
        
    def blink(self , count, time):
        for _ in range(count):
            gpio.output(self.pin, gpio.HIGH)
            sleep(time)
            gpio.output(self.pin, gpio.LOW)
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

leds = (led(16, "red"), led(21, "green"))

def ledRedFunction():
    def threadRun():
        leds[0].blink(10, 0.5)

    thread = Thread(target=threadRun, daemon=True)
    thread.start()

greenLedState = False

def ledGreenFunction():
    global greenLedState    # 함수 밖에 있는 변수를 가져다 쓰기 위한 global
    if greenLedState:
        leds[1].ledOff()
    else:
        leds[1].ledOn()
    greenLedState = not greenLedState

buttons = (Button(13, ledRedFunction), Button(6, ledGreenFunction))

try:
    while True:
        for button in buttons:
            button.waitPressed()

except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()