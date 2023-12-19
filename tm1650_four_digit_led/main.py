import machine
import time
import tm1650_four_digit_led

i2c = machine.I2C(0, sda=21, scl=22)

# Construct and initialize four digit TM1650 display
four_digit_led = tm1650_four_digit_led.Tm1650FourDigitLed(i2c=i2c)

while True:
    # Show digit 0 with decimal point
    four_digit_led.show_digit_number(0, 1, True)
    time.sleep_ms(500)

    # Show digit 1 without decimal point
    four_digit_led.show_digit_number(1, 2, False)
    time.sleep_ms(500)

    # Show more digits individually
    four_digit_led.show_digit_number(2, 3, True)
    time.sleep_ms(500)

    four_digit_led.show_digit_number(3, 4, False)
    time.sleep_ms(500)

    # Show integer number
    four_digit_led.show_number(1234)
    time.sleep_ms(500)

    # Show float number
    four_digit_led.show_number(56.78)
    time.sleep_ms(500)
