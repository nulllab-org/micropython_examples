from rgb_led import RgbLed
import time

rgb_led = RgbLed(pin_r=27, pin_g=26, pin_b=25)

colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (128, 0, 128),
    'orange': (255, 165, 0),
    'pink': (255, 192, 203),
    'cyan': (0, 255, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'brown': (139, 69, 19),
    'silver': (192, 192, 192),
    'gold': (255, 215, 0),
    'violet': (238, 130, 238),
}

while True:
    for color, value in colors.items():
        print('color:', color, ', value:', value)
        rgb_led.rgb(value[0], value[1], value[2])
        time.sleep_ms(500)
