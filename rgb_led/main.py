import machine
import time

g = machine.Pin(25, machine.Pin.OUT)
r = machine.Pin(26, machine.Pin.OUT)
b = machine.Pin(27, machine.Pin.OUT)

while True:
    r.off()
    g.off()
    b.off()
    time.sleep(1)

    r.on()
    g.off()
    b.off()
    time.sleep(1)

    r.off()
    g.on()
    b.off()
    time.sleep(1)

    r.off()
    g.off()
    b.on()
    time.sleep(1)
