import time
from machine import Pin
from config import KEYBOARD_ROW_PINS, KEYBOARD_COL_PINS

# 定义 row 按键引脚
row_pins = []
for p in KEYBOARD_ROW_PINS:
    row_pins.append(Pin(p, Pin.IN, Pin.PULL_UP))

# 定义 col 按键引脚
col_pins = []
for p in KEYBOARD_COL_PINS:
    col_pins.append(Pin(p, Pin.OUT))

# 去抖延时（毫秒）
DEBOUNCE_TIME = 50

# 上一次按键时间
last_key_time = 0


# 扫描键盘
def scan_keyboard():
    global last_key_time
    for col_index, col in enumerate(col_pins):
        # 将 col 置为低电平
        col.low()

        for row_index, row in enumerate(row_pins):
            # 如果 row 处于低电平，说明有键被按下
            if row.value() == 0:
                key = (row_index, col_index)
                current_time = time.time()
                # 检查是否有足够的去抖延时
                if current_time - last_key_time > DEBOUNCE_TIME / 1000:
                    last_key_time = current_time
                    return key
                else:
                    # 有时候会出现多次调用此处，原因不详
                    # 故把 last_key_time 置空，可以使得第二次调用变为成功
                    # last_key_time = 0
                    pass
        # 将列置为高电平，继续扫描下一列 col
        col.high()
    return None
