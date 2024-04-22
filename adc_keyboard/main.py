import time
from adc_keyboard import AdcKeyboard

adc_keyboard = AdcKeyboard(34)

keys = {
    'key A': AdcKeyboard.KEY_A,
    'key B': AdcKeyboard.KEY_B,
    'key C': AdcKeyboard.KEY_C,
    'key D': AdcKeyboard.KEY_D,
    'key E': AdcKeyboard.KEY_E,
}

print('please press the key')

while True:
    adc_keyboard.tick()  # must call the function to update in loop

    for key_name, key in keys.items():
        if adc_keyboard.pressed(key):
            print(key_name, 'pressed')
        if adc_keyboard.pressing(key):
            print(key_name, 'pressing')
        if adc_keyboard.released(key):
            print(key_name, 'released')
    time.sleep_ms(20)
