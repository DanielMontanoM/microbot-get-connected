def on_forever():
    if pins.digital_read_pin(DigitalPin.P1) == 1:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    elif pins.digital_read_pin(DigitalPin.P2) == 1:
        basic.show_leds("""
            # . . . #
                        # # # . #
                        # # . # #
                        # . # # #
                        # . . . #
        """)
    elif pins.digital_read_pin(DigitalPin.P7) == 1:
            basic.show_leds("""
                # . . . #
                            # # # . #
                            # # . # #
                            # . # # #
                            # . . . #
            """)
    
    elif pins.digital_read_pin(DigitalPin.P8) == 1:
            basic.show_leds("""
                # . . . #
                            # # # . #
                            # # . # #
                            # . # # #
                            # . . . #
            """)
    elif pins.digital_read_pin(DigitalPin.P9) == 1:
                    basic.show_leds("""
                        # . . . #
                                    # # # . #
                                    # # . # #
                                    # . # # #
                                    # . . . #
                    """)
    else:
        basic.show_leds("""
            # # # # #
                        # . # . #
                        # # # # #
                        # . . . #
                        # # # # #
        """)
basic.forever(on_forever)
