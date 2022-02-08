basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 1) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else if (pins.digitalReadPin(DigitalPin.P2) == 1) {
        basic.showLeds(`
            # . . . #
            # # # . #
            # # . # #
            # . # # #
            # . . . #
            `)
    } else if (pins.digitalReadPin(DigitalPin.P7) == 1) {
        basic.showLeds(`
            # . . . #
            # # # . #
            # # # . #
            # # # . #
            # # # . #
            `)
    } else {
        basic.showLeds(`
            # # # # #
            # . # . #
            # # # # #
            # . . . #
            # # # # #
            `)
    }
})
