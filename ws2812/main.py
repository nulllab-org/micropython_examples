import neopixel
import machine
import time

num_leds = 4
gpio = 26

neopixel = neopixel.NeoPixel(machine.Pin(26), num_leds)

neopixel[0] = (255, 0, 0)

neopixel[1] = (0, 255, 0)

neopixel[2] = (0, 0, 255)

neopixel[3] = (255, 0, 255)

neopixel.write()

while True:
    temp = neopixel[0]
    neopixel[0] = neopixel[1]
    neopixel[1] = neopixel[2]
    neopixel[2] = neopixel[3]
    neopixel[3] = temp
    neopixel.write()
    time.sleep(1)
