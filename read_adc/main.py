import machine
import time

gpio = 34
adc = machine.ADC(gpio, atten=machine.ADC.ATTN_11DB)

while True:
    adc_value = adc.read()
    print("gpio", gpio, "adc value:", adc_value)
    time.sleep_ms(100)
