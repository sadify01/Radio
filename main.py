def on_received_number_deprecated(receivedNumber):
    if receivedNumber == 0:
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.show_icon(IconNames.HEART)
radio.on_received_number_deprecated(on_received_number_deprecated)

def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(0)