import machine
import sys

gpio = 5
pin = machine.Pin(gpio, machine.Pin.OUT)

print('start')

while True:
    line = sys.stdin.readline()
    print("line content: ", line)
    if line == "on\n":
        print("trigger gpio", gpio, "on")
        pin.on()
    elif line == "off\n":
        print("trigger gpio", gpio, "off")
        pin.off()
