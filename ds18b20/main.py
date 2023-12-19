import ds18x20
import machine
import onewire
import time

dat = machine.Pin(5)

ds = ds18x20.DS18X20(onewire.OneWire(dat))

roms = ds.scan()
print('found devices:', roms)

while True:
    ds.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print('temperatures:', ds.read_temp(rom))
