from servo import Servo
import time

print('setup')

pin = 5
servo = Servo(pin)

print('loop')

while True:
    print('pin', pin, "set servo angle to 0")
    servo.angle = 0
    time.sleep(1)

    print('pin', pin, "set servo angle to 90")
    servo.angle = 90
    time.sleep(1)

    print('pin', pin, "set servo angle to 180")
    servo.angle = 180
    time.sleep(1)
