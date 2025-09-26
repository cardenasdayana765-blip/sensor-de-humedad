input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(humeda)
    if (humeda >= 1019) {
        basic.showIcon(IconNames.No)
    }
    
})
let humeda = 0
basic.showString("Humedad")
basic.forever(function on_forever() {
    
    humeda = pins.analogReadPin(AnalogReadWritePin.P1)
    if (humeda <= 1016) {
        basic.showIcon(IconNames.Heart)
        basic.clearScreen()
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
    
})
