import framebuf
from machine import Pin, I2C
import ssd1306
from fonts import matrix
from config import SSD_1306_I2C_ID, SSD_1306_SCL_PIN, SSD_1306_SDA_PIN, \
    SSD_1306_FREQ, SSD_OLED_WIDTH, SSD_OLED_HEIGHT, CHAR_WIDTH

# 设置 I2C 接口
i2c = I2C(SSD_1306_I2C_ID, scl=Pin(SSD_1306_SCL_PIN), sda=Pin(SSD_1306_SDA_PIN), freq=SSD_1306_FREQ)

# 初始化 OLED 屏幕
oled = ssd1306.SSD1306_I2C(SSD_OLED_WIDTH, SSD_OLED_HEIGHT, i2c)


def draw_oled(binary_matrix, pos_x, pos_y):
    buffer = bytearray(SSD_OLED_WIDTH * SSD_OLED_HEIGHT // 8)
    fb = framebuf.FrameBuffer(buffer, SSD_OLED_WIDTH, SSD_OLED_HEIGHT, framebuf.MONO_HLSB)

    # 遍历二进制矩阵，并在framebuf上设置相应的像素
    for y, row in enumerate(binary_matrix):
        for x in range(CHAR_WIDTH):
            pixel = (row >> (CHAR_WIDTH - 1 - x)) & 1
            fb.pixel(x, y, pixel)

    # 在OLED上显示framebuf中的内容，从左上角开始绘制
    oled.blit(fb, pos_x, pos_y)


line = 0
draw_pos_x = 0


def draw(str):
    global draw_pos_x
    global line

    oled.fill(0)
    line = 0
    draw_pos_x = 0

    for index, char in enumerate(str):
        if draw_pos_x < (SSD_OLED_WIDTH - 16):
            draw_pos_x = (index - 8 * line) * 16
        else:
            line = line + 1
            draw_pos_x = 0

        draw_pos_y = line * 16
        draw_oled(matrix[int(char)], draw_pos_x, draw_pos_y)
    oled.show()
