import ir_remote_control_receiver
import time

print('setup')

receiver = ir_remote_control_receiver.IRRemoteControlReceiver(pin=5)

button_str_dict = {
    ir_remote_control_receiver.BUTTON_0: "Button 0",
    ir_remote_control_receiver.BUTTON_1: "Button 1",
    ir_remote_control_receiver.BUTTON_2: "Button 2",
    ir_remote_control_receiver.BUTTON_3: "Button 3",
    ir_remote_control_receiver.BUTTON_4: "Button 4",
    ir_remote_control_receiver.BUTTON_5: "Button 5",
    ir_remote_control_receiver.BUTTON_6: "Button 6",
    ir_remote_control_receiver.BUTTON_7: "Button 7",
    ir_remote_control_receiver.BUTTON_8: "Button 8",
    ir_remote_control_receiver.BUTTON_9: "Button 9",
    ir_remote_control_receiver.BUTTON_POWER: "Button Power",
    ir_remote_control_receiver.BUTTON_MENU: "Button Menu",
    ir_remote_control_receiver.BUTTON_TEST: "Button Test",
    ir_remote_control_receiver.BUTTON_PLAY: "Button Play",
    ir_remote_control_receiver.BUTTON_VOLUME_UP: "Button Volume Up",
    ir_remote_control_receiver.BUTTON_VOLUME_DOWN: "Button Volume Down",
    ir_remote_control_receiver.BUTTON_PREVIOUS_PAGE: "Button previous page",
    ir_remote_control_receiver.BUTTON_NEXT_PAGE: "Button Next page",
    ir_remote_control_receiver.BUTTON_BACK: "Button Back",
    ir_remote_control_receiver.BUTTON_C: "Button C"
}

print("setup done")
print('start')

while True:
    receiver.receive()
    for button, button_str in button_str_dict.items():
        if receiver.pressed(button):
            print(button_str, 'pressed')
        if receiver.released(button):
            print(button_str, 'released')
        if receiver.pressing(button):
            print(button_str, 'pressing')
    time.sleep_ms(50)
