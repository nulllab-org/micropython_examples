from geek_servo_270 import GeekServo270
import time

print('setup')

pin = 5
geek_servo_270 = GeekServo270(pin)

print('loop')

while True:
    print('pin', pin, "set geek servo(270) angle to 0")
    geek_servo_270.angle = 0
    time.sleep(1)

    print('pin', pin, "set geek servo(270) angle to 90")
    geek_servo_270.angle = 90
    time.sleep(1)

    print('pin', pin, "set geek servo(270) angle to 180")
    geek_servo_270.angle = 180
    time.sleep(1)

    print('pin', pin, "set geek servo(270) angle to 270")
    geek_servo_270.angle = 270
    time.sleep(1)
