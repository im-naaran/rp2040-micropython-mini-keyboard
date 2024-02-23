import time
from machine import Pin
import neopixel
from draw import draw
from keyboard import scan_keyboard
from config import KEYCODE_MAP, CHAR_MAP, INDICATOR_LED

# 初始化 WS2812 LED
np = neopixel.NeoPixel(Pin(INDICATOR_LED), 1)

# 颜色定义
WHITE_COLOR = (255, 255, 255)


# 亮度的控制
def brightness(color, factor):
    r, g, b = color
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    return (r, g, b)


np[0] = brightness(WHITE_COLOR, 5 / 255)
np.write()

# oled 显示内容缓存
oled_char = ''

while True:
    key = scan_keyboard()
    if key is not None:
        row, col = key
        keycode = KEYCODE_MAP[row][col]
        char_name = CHAR_MAP[keycode]
        print(f"Key pressed: keycode={keycode}, char_name={char_name}, row={row}, col={col}")
        if char_name.isdigit():
            oled_char += char_name
        elif char_name == 'SP':
            oled_char += ' '
        elif char_name == 'EN':
            oled_char += '\n'
        elif char_name == 'BS':
            oled_char = oled_char[:-1]
        elif char_name == 'CL':
            oled_char = ''
        draw(oled_char)
    time.sleep(0.02)
