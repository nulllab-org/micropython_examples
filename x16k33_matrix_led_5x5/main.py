import arrow_image_5x5
import icon_image_5x5
import machine
import time
import x16k33_matrix_led_5x5

matrix_led_5x5 = x16k33_matrix_led_5x5.X16k33MatrixLed5x5(
    i2c=machine.I2C(0, sda=21, scl=22))

print('start')

while True:
    # show a single number
    matrix_led_5x5.show_number(1)
    time.sleep_ms(500)

    # show multiple digits
    matrix_led_5x5.show_number(9876)

    # show a single character
    matrix_led_5x5.show_string('z')
    time.sleep_ms(500)

    # show string
    matrix_led_5x5.show_string('abcd')
    time.sleep_ms(500)

    # show leds
    matrix_led_5x5.show_leds("""
    . . . . #
    . . . # .
    . . # . . 
    . # . . .
    # . . . #
    """)
    time.sleep_ms(500)

    # show icon
    matrix_led_5x5.show_icon(icon_image_5x5.Heart)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.SmallHeart)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Happy)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Sad)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Confused)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Angry)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Asleep)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Surprised)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Silly)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Fabulous)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Meh)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Yes)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.No)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Triangle)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.LeftTriangle)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Chessboard)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Diamond)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.SmallDiamond)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Square)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.SmallSquare)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Scissors)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.TShirt)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Rollerskate)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Duck)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.House)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Tortoise)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Butterfly)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.StickFigure)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Ghost)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Sword)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Giraffe)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Skull)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Umbrella)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Snake)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Rabbit)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Cow)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.QuarterNote)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.EighthNote)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Pitchfork)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(icon_image_5x5.Target)
    time.sleep_ms(500)

    # show arrows
    matrix_led_5x5.show_icon(arrow_image_5x5.North)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(arrow_image_5x5.NorthEast)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(arrow_image_5x5.East)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(arrow_image_5x5.SouthEast)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(arrow_image_5x5.South)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(arrow_image_5x5.SouthWest)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(arrow_image_5x5.West)
    time.sleep_ms(500)
    matrix_led_5x5.show_icon(arrow_image_5x5.NorthWest)
    time.sleep_ms(500)
