
from machine import SPI,Pin,I2C
import time
import gt20l #导入库
import ssd1306

cs=Pin(15,Pin.OUT) #定义cs引脚

spi=SPI(-1,mosi=Pin(13),miso=Pin(12),sck=Pin(14)) #定义spi对象
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

gt20l=gt20l.gt20l(spi,cs) #定义gt20l对象
lcd=ssd1306.SSD1306_I2C(128,64,i2c)

t='Hello gt20l'
x_a=0
y_a=0
off_set=0
for x in t:
  data=gt20l.get_816ascll(x)
  data=list(map(lambda x:bin(int(x,16)).replace('0b',''),data))
  data=list(map(lambda x:'0'*(8-len(x))+x,data))
  for x in range(8):
    for y in range(8):
      lcd.pixel(x_a+(8*off_set)+x,y_a+y,int(data[x][7-y]))
  for x in range(8):
    for y in range(8):
      lcd.pixel(x_a+(8*off_set)+x,y_a+y+8,int(data[x+8][7-y]))
  off_set+=1
lcd.show()
