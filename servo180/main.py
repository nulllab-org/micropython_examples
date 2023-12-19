import servo180
import time

print('setup')
gpio = 5
servo = servo180.Servo180(pin=5)

print('setup done')
print('start')

while True:
    print('gpio', gpio, "set servo180 angle to 0")
    servo.set_angle(0)
    time.sleep(1)

    print('gpio', gpio, "set servo180 angle to 90")
    servo.set_angle(90)
    time.sleep(1)

    print('gpio', gpio, "set servo180 angle to 180")
    servo.set_angle(180)
    time.sleep(1)
