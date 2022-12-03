input.onButtonPressed(Button.A, function () {
    shouldWriteToSerial = !(shouldWriteToSerial)
})
let activeRange: neopixel.Strip = null
let shouldWriteToSerial = false
VL53L1X.init()
let strip = neopixel.create(DigitalPin.P8, 16, NeoPixelMode.RGB)
// value for distance that shows all leds
let lowThreshold = 150
// value for distance that turns all leds off
let highTreshold = 1500
basic.forever(function () {
    if (shouldWriteToSerial) {
        serial.writeLine("" + VL53L1X.readSingle())
    }
    strip.clear()
    activeRange = strip.range(0, Math.map(VL53L1X.readSingle(), lowThreshold, highTreshold, 16, 0))
    activeRange.showColor(neopixel.colors(NeoPixelColors.Red))
    basic.pause(100)
})
