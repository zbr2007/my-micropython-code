
from machine import SPI,Pin,I2C
import time
import gt20l #导入库
import ssd1306

cs=Pin(15,Pin.OUT) #定义cs引脚
spi=SPI(-1,mosi=Pin(13),miso=Pin(12),sck=Pin(14)) #定义spi对象
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

gt20l=gt20l.gt20l(spi,cs) #定义gt20l对象
lcd=ssd1306.SSD1306_I2C(128,64,i2c)

data=gt20l.get_gb2312_font([0xb9,0xfa]) #0xb9是"国"在gb2312编码中高八位，0xfa是低八位
data=list(map(lambda x:bin(int(x,16)).replace('0b',''),data))
data=list(map(lambda x:'0'*(8-len(x))+x,data))

data1=data[0:15]
data2=data[16:31]

for x in range(15):
  for y in range(8):
    lcd.pixel(x,y,int(data1[x][7-y]))
for x in range(15):
  for y in range(8):
    lcd.pixel(x,y+8,int(data2[x][7-y]))
lcd.show()
