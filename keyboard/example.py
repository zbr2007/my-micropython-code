
from machine import Pin,I2C
import ssd1306
import keyboard
import time

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

lcd=ssd1306.SSD1306_I2C(128,64,i2c)
k=keyboard.keyboard(lcd) #初始化键盘对象,要带上ssd1306对象
k.init('title') #键盘的标题(不一定要定义)
lcd.show()
for x in range(5):
  time.sleep(0.2)
  k.moveDown()
  lcd.show()
  print('moveDown:',k.zb,k.get())
for x in range(5):
  time.sleep(0.2)
  k.moveUp()
  lcd.show()
  print('moveUp',k.zb,k.get())
for x in range(5):
  time.sleep(0.2)
  k.moveRight()
  lcd.show()
  print('moveRight',k.zb,k.get())
for x in range(5):
  time.sleep(0.2)
  k.moveLeft()
  lcd.show()
  print('moveLeft',k.zb,k.get())
print(k.get())

