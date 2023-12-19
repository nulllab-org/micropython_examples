import machine
import time

gpio = 5
interval_ms = 1000
pin = machine.Pin(gpio, machine.Pin.OUT)

while True:
    pin.on()
    print("gpio", gpio, "on")
    time.sleep_ms(interval_ms)

    pin.off()
    print("gpio", gpio, "off")
    time.sleep_ms(interval_ms)
