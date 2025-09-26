def on_button_pressed_a():
    basic.show_number(humeda)
    if humeda >= 1019:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

humeda = 0
basic.show_string("Humedad")

def on_forever():
    global humeda
    humeda = pins.analog_read_pin(AnalogReadWritePin.P1)
    if humeda <= 1016:
        basic.show_icon(IconNames.HEART)
        basic.clear_screen()
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
