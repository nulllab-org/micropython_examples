import machine
import ssd1306
import time

# using default address 0x3C
i2c = machine.I2C(0, sda=21, scl=22)

display = ssd1306.SSD1306_I2C(128, 64, i2c)

count = 0

while True:
    display.fill(0)
    display.text('Hello, World!', 0, 0, 1)
    display.text("count:" + str(count), 0, 32, 1)
    display.show()
    count += 1
    time.sleep(1)
