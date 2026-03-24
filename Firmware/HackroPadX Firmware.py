import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeConfiguration
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.oled import OLED, OLED_DisplayMode

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4, board.D5)
keyboard.diode_orientation = DiodeConfiguration.COL2ROW

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.D6, board.D7, board.D8),)

oled = OLED(
    scl=board.SCL,
    sda=board.SDA,
    width=128,
    height=64,
    flip=False,
    display_mode=OLED_DisplayMode.TXT
)
keyboard.extensions.append(oled)

keyboard.extensions.append(MediaKeys())

layers = Layers()
keyboard.modules.append(layers)

keyboard.keymap = [
    [
        KC.VOLU, KC.MUTE, KC.VOLD,
        KC.MPRV, KC.PLAY, KC.MNXT,
        KC.COPY, KC.PASTE, KC.CUT,
    ],
]

encoder_handler.map = [(
    (KC.VOLU, KC.VOLD),
    KC.MUTE,
)]

def update_oled():
    oled.text("HacroPadX", 0, 0, 1)
    oled.text("Layer: 0", 0, 12, 1)
    oled.text("Vol: " + str(keyboard.active_layers[0]), 0, 24, 1)
    oled.show()

update_oled()

if __name__ == '__main__':
    keyboard.go()