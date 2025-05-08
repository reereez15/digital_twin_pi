import RPi.GPIO as gpio
from time import sleep

ledpin = (16,21)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
for pin in ledpin:
    gpio.setup(pin, gpio.OUT)


currentPassword = None

while True:
    newPassword = input("new password: ")
    confirmPassword = input("confirm password: ")
    if newPassword == confirmPassword:
        currentPassword = newPassword
        print("0")
        break
    else :
        print("x")

while True:
    loginPassword = input("login password: ")
    if loginPassword == currentPassword:
        gpio.output(ledpin[0], gpio.HIGH)
        break
    else :
        for i in range(5):
            gpio.output(ledpin[1], gpio.HIGH)
            sleep(0.1)
            gpio.output(ledpin[1], gpio.LOW)
            sleep(0.1)

