import machine
import time

x = machine.ADC(27, atten=machine.ADC.ATTN_11DB)
y = machine.ADC(26, atten=machine.ADC.ATTN_11DB)
button = machine.Pin(25, machine.Pin.IN)

print("start")

while True:
    x_value = x.read()
    y_value = y.read()
    button_value = button.value()
    print("x:", x_value, ", y:", y_value, ", button: ", button_value)
    time.sleep_ms(100)
