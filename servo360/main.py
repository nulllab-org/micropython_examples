import servo360
import time

print('setup')

gpio = 5
servo360 = servo360.Servo360(pin=gpio)

print('setup done')
print('start')

while True:
    print('gpio', gpio, 'servo360 start forward')
    servo360.start_forward()
    time.sleep(1)

    print('gpio', gpio, 'servo360 stop')
    servo360.stop()
    time.sleep(1)

    print('gpio', gpio, 'servo360 start reverse')
    servo360.start_reverse()
    time.sleep(1)
