#导入库
from machine import Pin,I2C
import ssd1306
import keyboard

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000) #创建i2c对象
lcd=ssd1306.SSD1306_I2C(128,64,i2c) #创建oled屏对象

k=keyboard.keyboard(lcd) #创建keyboard对象
k.init() #初始化键盘
lcd.show() #将键盘显示到屏幕上
