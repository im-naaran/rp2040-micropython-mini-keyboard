# 主循环扫描间隔（秒）
MAIN_LOOP_INTERVAL = 0.01

# 指示灯
INDICATOR_LED = 16

# ssd 1306 屏幕设置
SSD_1306_I2C_ID = 1
SSD_1306_SCL_PIN = 27
SSD_1306_SDA_PIN = 26
SSD_1306_FREQ = 400000
SSD_OLED_WIDTH = 128
SSD_OLED_HEIGHT = 64

# 每个字符宽度
CHAR_WIDTH = 16

# 键盘设置
KEYBOARD_ROW_PINS = [5, 6, 7, 8]
KEYBOARD_COL_PINS = [4, 3, 2, 1]

# 键盘去抖时间（毫秒）
KEYBOARD_DEBOUNCE_TIME = 50

# 按键键位映射
KEYCODE_MAP = [
    ['S16', 'S15', 'S14', 'S13'],
    ['S12', 'S11', 'S10', 'S9'],
    ['S8', 'S7', 'S6', 'S5'],
    ['S4', 'S3', 'S2', 'S1'],
]

# 按键值映射
CHAR_MAP = {
    'S1': '1',
    'S2': '2',
    'S3': '3',
    'S4': '4',
    'S5': '5',
    'S6': '6',
    'S7': '7',
    'S8': '8',
    'S9': '9',
    'S10': '0',
    'S11': 'BS',
    'S12': 'CL',
    'S13': 'SP',
    'S14': 'EN',
    'S15': '',
    'S16': '',
}
