import servo360
import time

print('setup')

# gpio_5 = 5
servo360_4 = servo360.Servo360(pin=5)
servo360_4.run_speed(80)
# gpio_4 = 4
# servo360_5 = servo360.Servo360(pin=5)

print('setup done')
print('start')

while True:
    servo360_4.run_speed(100)
    # print('gpio', gpio, 'servo360 start forward')
    # servo360_4.start_forward()
    # servo360_5.start_forward()
    # servo3604.start_forward()
    # time.sleep(1)

    # print('gpio', gpio, 'servo360 stop')
    # servo360.stop()
    # time.sleep(1)

    # print('gpio', gpio, 'servo360 start reverse')
    # servo360.start_reverse()
    # time.sleep(1)
