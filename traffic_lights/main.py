import machine
import time

g_light = machine.Pin(33, machine.Pin.OUT)
y_light = machine.Pin(32, machine.Pin.OUT)
r_light = machine.Pin(23, machine.Pin.OUT)

while True:
    g_light.on()
    y_light.on()
    r_light.on()
    time.sleep_ms(500)

    g_light.off()
    y_light.off()
    r_light.off()
    time.sleep_ms(500)

    g_light.on()
    y_light.off()
    r_light.off()
    time.sleep_ms(500)

    g_light.off()
    y_light.on()
    r_light.off()
    time.sleep_ms(500)

    g_light.off()
    y_light.off()
    r_light.on()
    time.sleep_ms(500)
