# micropython_examples

| sensors | examples | work port |
| --- | --- | --- |
| LED White | [write_digital/main.py](write_digital/main.py) | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| Traffic light module | [rgb_led/main.py](rgb_led/main.py) | [25, 26, 27, 3V3, G]</br>[23, 32, 33, 3V3, G] |
| Tactile switch button | [read_digital/main.py](read_digital/main.py) | [4, 3V3, G]</br> [5, 3V3, G]</br> [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| Passive piezo buzzer | [passive_buzzer/main.py](passive_buzzer/main.py) | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| Photoresistor sensor | [read_adc/main.py](read_adc/main.py) | [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| Ultrasonic sensor | [ultrasonic_one_wire/main.py](ultrasonic_one_wire/main.py) | [5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br>
| Potentiometer (rotary) | [read_adc/main.py](read_adc/main.py) | [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| Servo motor (180 degree) | [servo/main.py](servo/main.py)  | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| Geek Servo motor (270 degree) | [geek_servo_270/main.py](geek_servo_270/main.py)  | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| Servo motor (Lego, 360 degree) | [servo360/main.py](servo360/main.py)  | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| RGB LED | [rgb_led/main.py](rgb_led/main.py) | [25, 26, 27, 3V3, G]</br>[23, 32, 33, 3V3, G] |
| 5x5 Dot matrix | [x16k33_matrix_led_5x5/main.py](x16k33_matrix_led_5x5/main.py) | [SCL, SDA, 5V, G] |
| Temperature sensor (DS18B20) | [ds18b20/main.py](ds18b20/main.py) | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| IR proximity sensor | [read_adc/main.py](read_adc/main.py) | [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| PIR motion sensor | [read_digital/main.py](read_digital/main.py) |[4, 3V3, G]</br> [5, 3V3, G]</br> [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| DHT11 sensor | [dht11/main.py](dht11/main.py) | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| OLED (128*64) | [ssd1306_i2c_128x64/main.py](ssd1306_i2c_128x64/main.py) | [SCL, SDA, 5V, G] |
| DC motor | [dc_motor/main.py](dc_motor/main.py) | [12, 13, 5V, G]</br>[14, 15, 5V, G]</br> |
| Sound sensor | [read_digital_and_adc/main.py](read_digital_and_adc/main.py) | [12, 13, 5V, G]</br>[14, 15, 5V, G]</br>[19, 39, 3V3, G]</br>[18, 36, 3V3, G] |
| Joystick | [joystick/main.py](joystick/main.py) | [25, 26, 27, 3V3, G]</br>[23, 32, 33, 3V3, G] |
| 4 digit 7 segment | [tm1650_four_digit_led/main.py](tm1650_four_digit_led/main.py) | [SCL, SDA, 5V, G] |
| IR Receiver & IR remote controller | [ir_remote_control_receiver/main.py](ir_remote_control_receiver/main.py) | [4, 3V3, G]</br>[5, 3V3, G]</br> [25, 3V3, G]</br>[26, 3V3, G]</br>[34, 3V3, G]</br>[35, 3V3, G]</br>**[36, 3V3, G]**</br>**[39, 3V3, G]**</br> |
| Touch sensor  | [read_digital/main.py](read_digital/main.py) | [4, 3V3, G]</br> [5, 3V3, G]</br> [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| Tilt sensor | [read_digital/main.py](read_digital/main.py) | [4, 3V3, G]</br> [5, 3V3, G]</br> [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| Shock sensor | [read_digital_and_adc/main.py](read_digital_and_adc/main.py) | [12, 13, 5V, G]</br>[14, 15, 5V, G]</br>[19, 39, 3V3, G]</br>[18, 36, 3V3, G] |
| Neopixel | [ws2812/main.py](ws2812/main.py) | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| Soil moisture sensor | [read_adc/main.py](read_adc/main.py) | [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| Steam sensor (Water vapor sensor) | [read_adc/main.py](read_adc/main.py) | [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| Flame sensor | [read_digital_and_adc/main.py](read_digital_and_adc/main.py) | [12, 13, 5V, G]</br>[14, 15, 5V, G]</br>[19, 39, 3V3, G]</br>[18, 36, 3V3, G] |
| Gas sensor | [read_digital_and_adc/main.py](read_digital_and_adc/main.py) | [12, 13, 5V, G]</br>[14, 15, 5V, G]</br>[19, 39, 3V3, G]</br>[18, 36, 3V3, G] |
| 5V relay module | [write_digital/main.py](write_digital/main.py) | [4, 3V3, G]</br>[5, 3V3, G]</br>[25, 3V3, G]</br>[26, 3V3, G]</br> |
| 4 buttons module | [read_adc/main.py](read_adc/main.py) | [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
| qma6100p 3-axis accelerometer | [qma6100p/measure_gesture/main.py](qma6100p/measure_gesture/main.py)</br>[qma6100p/read_acceleration/main.py](qma6100p/read_acceleration/main.py) | [SCL, SDA, 5V, G] |
| adc five button | [adc_five_button/main.py](adc_five_button/main.py) | [25, 3V3, G]</br> [26, 3V3, G]</br>  [34, 3V3, G]</br>[35, 3V3, G]</br> [36, 3V3, G]</br> [39, 3V3, G]</br> |
