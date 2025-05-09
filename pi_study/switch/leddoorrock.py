import RPi.GPIO as gpio
from time import sleep

class led:
    def __init__(self, pin, color):
        self.pin = pin
        self.color = color
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, gpio.LOW)

    def blink(self, count, time):
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

leds = (led(16, "red"), led(20, "green"), led(21,"yellow"))

redLedState = False
greenLedState = False
yellowLedState = False

def ledRedFunction():
    global redLedState
    if redLedState:
        leds[0].ledOff()
    else:
        leds[0].ledOn()
    redLedState = not redLedState

def ledGreenFunction():
    global greenLedState
    if greenLedState:
        leds[1].ledOff()
    else:
        leds[1].ledOn()
    greenLedState = not greenLedState

def ledYellowFunction():
    global yellowLedState
    if yellowLedState:
        leds[2].ledOff()
    else:
        leds[2].ledOn()
    yellowLedState = not yellowLedState

buttons = (Button(13, ledRedFunction), Button(19, ledGreenFunction),
           Button(26, ledYellowFunction))

currentPassword = None

while True:
    newPassword = input("new password: ")
    confirmPassword = input("confirm password: ")
    if newPassword == confirmPassword:
        currentPassword = newPassword
        print("비밀번호가 설정되었습니다.")
        break
    else:
        print("비밀번호가 틀렸습니다.")

while True:
    loginPassword = input("login password: ")
    if loginPassword == currentPassword:
        for i in range(3):
            gpio.output(leds[0], gpio.HIGH)
            sleep(0.1)
            gpio.output(leds[0], gpio.LOW)
            sleep(0.1)
            gpio.output(leds[1], gpio.HIGH)
            sleep(0.1)
            gpio.output(leds[1], gpio.LOW)
            sleep(0.1)
            gpio.output(leds[2], gpio.HIGH)
            sleep(0.1)
            gpio.output(leds[2], gpio.LOW)
            sleep(0.1)
    else:
        for i in range(3):
            gpio.output(leds[0], gpio.HIGH)
            gpio.output(leds[1], gpio.HIGH)
            gpio.output(leds[2], gpio.HIGH)
            sleep(0.1)
            gpio.output(leds[0], gpio.LOW)
            gpio.output(leds[1], gpio.LOW)
            gpio.output(leds[2], gpio.LOW)

