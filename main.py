import time
from draw import draw
from keyboard import scan_keyboard
from config import KEYCODE_MAP, CHAR_MAP

# oled 显示内容缓存
oled_char = ''

while True:
    key = scan_keyboard()
    if key is not None:
        row, col = key
        keycode = KEYCODE_MAP[row][col]
        char_name = CHAR_MAP[keycode]
        print(f"Key pressed: keycode={keycode}, char_name={char_name}")
        if char_name.isdigit():
            oled_char += char_name
        if char_name == 'BS':
            oled_char = oled_char[:-1]
        elif char_name == 'CL':
            oled_char = ''
        draw(oled_char)
    time.sleep(0.02)
