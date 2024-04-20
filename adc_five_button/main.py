import time
from adc_five_button import AdcFiveButton

adc_five_button = AdcFiveButton(34)

buttons = {
    'button a': AdcFiveButton.BUTTON_A,
    'button b': AdcFiveButton.BUTTON_B,
    'button c': AdcFiveButton.BUTTON_C,
    'button d': AdcFiveButton.BUTTON_D,
    'button e': AdcFiveButton.BUTTON_E,
}

print('please press the button')

while True:
    adc_five_button.tick()  # must call the function to update in loop

    for button_name, button in buttons.items():
        if adc_five_button.pressed(button):
            print(button_name, 'pressed')
        if adc_five_button.pressing(button):
            print(button_name, 'pressing')
        if adc_five_button.released(button):
            print(button_name, 'released')
    time.sleep_ms(20)
