import machine
import time

gpio_digital = 14
gpio_adc = 15

pin = machine.Pin(gpio_digital, machine.Pin.IN)
adc = machine.ADC(gpio_adc, atten=machine.ADC.ATTN_11DB)

while True:
    digital_value = pin.value()
    adc_value = adc.read()
    print("gpio", gpio_digital, "digital value:", digital_value, ", gpio", gpio_adc, "adc value:", adc_value)
    time.sleep_ms(100)
