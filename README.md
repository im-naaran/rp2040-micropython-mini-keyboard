# RP2040 MicroPython 迷你键盘

一个基于 RP2040 和 MicroPython 的迷你数字键盘项目，通过矩阵键盘输入数字，在 SSD1306 OLED 屏幕上显示。

## 硬件要求

- RP2040 开发板（如 Raspberry Pi Pico）
- 4x4 矩阵键盘
- SSD1306 OLED 显示屏（128x64）
- WS2812 LED 指示灯（可选）

## 引脚连接

### 矩阵键盘
- 行引脚：GPIO 5, 6, 7, 8
- 列引脚：GPIO 4, 3, 2, 1

### SSD1306 OLED
- SCL：GPIO 27
- SDA：GPIO 26

### 指示灯
- WS2812：GPIO 16

## 功能特性

- 数字输入（0-9）
- 空格键（SP）
- 换行键（EN）
- 退格键（BS）
- 清除键（CL）

## 文件结构

```
├── main.py          # 主程序入口
├── keyboard.py      # 键盘扫描模块
├── draw.py          # OLED显示模块
├── fonts.py         # 字体数据
├── config.py        # 配置文件
├── lib/
│   └── ssd1306.py  # SSD1306驱动库
└── README.md
```

## 使用方法

1. 将代码上传到 RP2040 开发板
2. 连接硬件组件
3. 运行 `main.py`
4. 使用矩阵键盘输入数字

## 技术细节

- 使用 MicroPython 开发
- 主循环扫描频率：100Hz (10ms间隔)
- 按键去抖时间：50ms
- OLED 显示分辨率：128x64

## 配置参数

主要配置参数位于 `config.py` 文件中：

- `MAIN_LOOP_INTERVAL`: 主循环扫描间隔（默认0.01秒）
- `KEYBOARD_DEBOUNCE_TIME`: 按键去抖时间（默认50毫秒）
- `KEYBOARD_ROW_PINS`: 键盘行引脚配置
- `KEYBOARD_COL_PINS`: 键盘列引脚配置

可根据实际需求调整这些参数以优化性能和响应性。
