def on_button_pressed_a():
    global shouldWriteToSerial
    shouldWriteToSerial = not (shouldWriteToSerial)
input.on_button_pressed(Button.A, on_button_pressed_a)

activeRange: neopixel.Strip = None
shouldWriteToSerial = False
VL53L1X.init()
strip = neopixel.create(DigitalPin.P8, 16, NeoPixelMode.RGB)
lowThreshold = 150
highTreshold = 1000

def on_forever():
    global activeRange,lowThreshold,highTreshold
    if shouldWriteToSerial:
        serial.write_line("" + str(VL53L1X.read_single()))
    strip.clear()
    activeRange = strip.range(0, Math.map(VL53L1X.read_single(), lowThreshold, highTreshold, 16, 0))
    activeRange.show_color(neopixel.colors(NeoPixelColors.RED))
    basic.pause(100)
basic.forever(on_forever)
