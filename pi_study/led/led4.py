import RPi.GPIO as gpio
from time import sleep

ledpin1 = 16
ledpin2 = 21

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(ledpin1, gpio.OUT)
gpio.setup(ledpin2, gpio.OUT)

currentPassword = None

while True:
    newPassword = input("new password: ")
    confirmPassword = input("confirm password: ")
    if newPassword == confirmPassword:
        currentPassword = newPassword
        print("o")
        break
    else :
        print("x")

while True:
    loginPassword = input("login password: ")
    if currentPassword == loginPassword:
        gpio.output(ledpin1, gpio.HIGH)
        break
    else :
        for i in range(5):
            gpio.output(ledpin2, gpio.HIGH)
            sleep(0.1)
            gpio.output(ledpin2, gpio.LOW)
            sleep(0.1)
        
