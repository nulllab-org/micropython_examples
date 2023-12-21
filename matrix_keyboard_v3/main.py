from matrix_keyboard_v3 import MatrixKeyboardV3
import machine
import time

keyboard = MatrixKeyboardV3(i2c=machine.I2C(0))

keys_dict = {
    MatrixKeyboardV3.KEY_1: "key 1",
    MatrixKeyboardV3.KEY_2: "key 2",
    MatrixKeyboardV3.KEY_3: "key 3",
    MatrixKeyboardV3.KEY_A: "key A",
    MatrixKeyboardV3.KEY_4: "key 4",
    MatrixKeyboardV3.KEY_5: "key 5",
    MatrixKeyboardV3.KEY_6: "key 6",
    MatrixKeyboardV3.KEY_B: "key B",
    MatrixKeyboardV3.KEY_7: "key 7",
    MatrixKeyboardV3.KEY_8: "key 8",
    MatrixKeyboardV3.KEY_9: "key 9",
    MatrixKeyboardV3.KEY_C: "key C",
    MatrixKeyboardV3.KEY_ASTERISK: "key *",
    MatrixKeyboardV3.KEY_0: "key 0",
    MatrixKeyboardV3.KEY_NUMBER_SIGN: "key #",
    MatrixKeyboardV3.KEY_D: "key D",
}

while True:
    keyboard.update()
    for key, value in keys_dict.items():
        if keyboard.pressed(key):
            print(value, "pressed")
        if keyboard.pressing(key):
            print(value, "pressing")
        if keyboard.released(key):
            print(value, "released")
    time.sleep_ms(10)
