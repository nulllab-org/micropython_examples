import time
import ultrasonic_one_wire

ultrasonic = ultrasonic_one_wire.UltrasonicOneWire(io_pin=25)
print('start')

while True:
    distance_cm = ultrasonic.distance_cm()
    print("distance:", distance_cm, "cm")
    time.sleep_ms(100)
