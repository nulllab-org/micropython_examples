import arrow_image_5x5
import icon_image_5x5
import machine
import time
import x16k33_matrix_led_5x5

matrix_led_5x5 = x16k33_matrix_led_5x5.X16k33MatrixLed5x5(i2c=machine.I2C(0, sda=21, scl=22))

while True:
    # show a single number
    matrix_led_5x5.show_number(1)
    time.sleep(1)

    # show multiple digits
    matrix_led_5x5.show_number(9876)
    # time.sleep(1)

    # show a single character
    matrix_led_5x5.show_string('z')
    time.sleep(1)

    # show string
    matrix_led_5x5.show_string('1234')
    time.sleep(1)

    # show leds
    matrix_led_5x5.show_leds("""
    . . . . #
    . . . # .
    . . # . . 
    . # . . .
    # . . . #
    """)
    time.sleep(1)

    # show icon
    matrix_led_5x5.show_icon(icon_image_5x5.Heart)
    time.sleep(1)

    # show arrow
    matrix_led_5x5.show_icon(arrow_image_5x5.North)
    time.sleep(1)
