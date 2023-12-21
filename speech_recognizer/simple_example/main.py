from speech_recognizer import SpeechRecognizer
import machine

speech_recognizer = SpeechRecognizer(i2c=machine.I2C(0, scl=22, sda=21))
speech_recognizer.add_keyword(0, "xiao yi xiao yi")
speech_recognizer.add_keyword(1, "bei jing")
speech_recognizer.add_keyword(2, "chong qing")
speech_recognizer.add_keyword(3, "cheng du")
speech_recognizer.add_keyword(4, "shang hai")

print("entry loop")

while True:
    result = speech_recognizer.recognize()
    if result >= 0:
        print("speech recognition result:", result)

    event = speech_recognizer.get_event()
    if event != SpeechRecognizer.EVENT_NONE:
        print("event: %d" % event)
