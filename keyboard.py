import time
from machine import Pin
from config import KEYBOARD_ROW_PINS, KEYBOARD_COL_PINS, KEYBOARD_DEBOUNCE_TIME

# 定义 row 按键引脚
row_pins = []
for p in KEYBOARD_ROW_PINS:
    row_pins.append(Pin(p, Pin.IN, Pin.PULL_UP))

# 定义 col 按键引脚
col_pins = []
for p in KEYBOARD_COL_PINS:
    col_pins.append(Pin(p, Pin.OUT))

# 去抖延时（毫秒）
DEBOUNCE_TIME = KEYBOARD_DEBOUNCE_TIME

# 按键状态记录
key_states = {}
last_key_time = 0

# 初始化所有列为高电平
def init_keyboard():
    for col in col_pins:
        col.high()

# 扫描键盘
def scan_keyboard():
    global last_key_time, key_states
    
    current_time = time.ticks_ms()
    
    for col_index, col in enumerate(col_pins):
        # 将当前列置为低电平
        col.low()
        
        # 短暂延时确保信号稳定
        time.sleep_us(100)
        
        for row_index, row in enumerate(row_pins):
            key = (row_index, col_index)
            
            # 读取按键状态
            is_pressed = (row.value() == 0)
            
            # 检查按键状态变化
            if key not in key_states:
                key_states[key] = False
            
            # 如果按键状态发生变化且被按下
            if is_pressed and not key_states[key]:
                # 检查去抖时间
                if current_time - last_key_time > DEBOUNCE_TIME:
                    key_states[key] = True
                    last_key_time = current_time
                    col.high()  # 恢复列状态
                    return key
            
            # 如果按键释放，更新状态
            elif not is_pressed and key_states[key]:
                key_states[key] = False
        
        # 将列恢复为高电平
        col.high()
    
    return None

# 初始化键盘
init_keyboard()
