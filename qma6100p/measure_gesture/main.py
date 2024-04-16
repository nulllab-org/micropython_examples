import machine
from qma6100p import Qma6100p
from accelerometer import Accelerometer

i2c = machine.I2C(0, sda=21, scl=22)
accelerometer = Qma6100p(i2c)

shake_count = 0

while True:
    accelerometer.tick()

    if accelerometer.gesture_changed:
        if accelerometer.gesture == Accelerometer.GESTURE_X_POSITIVE_TILT:
            print('GESTURE_X_POSITIVE_TILT')
        elif accelerometer.gesture == Accelerometer.GESTURE_X_NEGATIVE_TILT:
            print('GESTURE_X_NEGATIVE_TILT')
        elif accelerometer.gesture == Accelerometer.GESTURE_Y_POSITIVE_TILT:
            print('GESTURE_Y_POSITIVE_TILT')
        elif accelerometer.gesture == Accelerometer.GESTURE_Y_NEGATIVE_TILT:
            print('GESTURE_Y_NEGATIVE_TILT')
        elif accelerometer.gesture == Accelerometer.GESTURE_FACE_UP:
            print('GESTURE_FACE_UP')
        elif accelerometer.gesture == Accelerometer.GESTURE_FACE_DOWN:
            print('GESTURE_FACE_DOWN')
        else:
            print('GESTURE_NONE')
    elif accelerometer.gesture == Accelerometer.GESTURE_SHAKE:
        shake_count += 1
        print('GESTURE_SHAKE', shake_count)
    # print(accelerometer._accelerations)
    # time.sleep_ms(10)
