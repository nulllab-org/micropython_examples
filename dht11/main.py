import dht
import machine
import time

dht_sensor = dht.DHT11(machine.Pin(5, machine.Pin.OUT))

print("start")

while True:
    dht_sensor.measure()
    print("temperature:", dht_sensor.temperature(), ", humidity:",
          dht_sensor.humidity())
    time.sleep(1)
