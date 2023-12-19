import machine
import time

gpio_pin = 35
pin = machine.Pin(gpio_pin, machine.Pin.IN)

print('start')

while True:
    digital_value = pin.value()
    print("gpio", gpio_pin, "digital_value:", digital_value)
    time.sleep_ms(100)