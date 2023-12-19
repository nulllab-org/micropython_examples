import machine
import time

print("setup")

pin_a = machine.Pin(14, machine.Pin.OUT)
pin_b = machine.Pin(15, machine.Pin.OUT)

print("setup done")
print("start")

while True:
    print('start forward')
    pin_a.on()
    pin_b.off()
    time.sleep(1)

    print('start reserve')
    pin_a.off()
    pin_b.on()
    time.sleep(1)
