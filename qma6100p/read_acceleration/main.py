import machine
from qma6100p import Qma6100p
import time

i2c = machine.I2C(0, sda=21, scl=22)
accelerometer = Qma6100p(i2c)

while True:
    accelerometer.tick()
    print(f'x:{accelerometer.x:5d}, y:{accelerometer.y:5d}, z:{accelerometer.z:5d}')
    time.sleep_ms(50)
