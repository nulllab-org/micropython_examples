import buzzer
import time

buzzer = buzzer.Buzzer(pin=25)

tones = (262, 262, 392, 392, 440, 440, 392)

print("start")

while True:
    for tone in tones:
        buzzer.pitch_ms(tone, 400)
        time.sleep_ms(100)
