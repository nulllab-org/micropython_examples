import machine
from qma6100p import Qma6100p
from accelerometer import Accelerometer

i2c = machine.I2C(0, sda=21, scl=22)
accelerometer = Qma6100p(i2c)

changed_count = 0

while True:
    accelerometer.tick()

    if accelerometer.posture_changed:
        changed_count += 1
        if accelerometer.posture == Accelerometer.POSTURE_X_POSITIVE_TILT:
            print(f'[{changed_count}] posture: x positive tilt')
        elif accelerometer.posture == Accelerometer.POSTURE_X_NEGATIVE_TILT:
            print(f'[{changed_count}] posture: x negative tilt')
        elif accelerometer.posture == Accelerometer.POSTURE_Y_POSITIVE_TILT:
            print(f'[{changed_count}] posture: y positive tilt')
        elif accelerometer.posture == Accelerometer.POSTURE_Y_NEGATIVE_TILT:
            print(f'[{changed_count}] posture: y negative tilt')
        elif accelerometer.posture == Accelerometer.POSTURE_FACE_UP:
            print(f'[{changed_count}] posture: face up')
        elif accelerometer.posture == Accelerometer.POSTURE_FACE_DOWN:
            print(f'[{changed_count}] posture: face down')
        elif accelerometer.posture == Accelerometer.POSTURE_FREE_FALL:
            print(f'[{changed_count}] posture: free fall')
        elif accelerometer.posture == Accelerometer.POSTURE_SHAKE:
            print(f'[{changed_count}] posture: shake')
        elif accelerometer.posture == Accelerometer.POSTURE_NONE:
            print(f'[{changed_count}] posture: none')
