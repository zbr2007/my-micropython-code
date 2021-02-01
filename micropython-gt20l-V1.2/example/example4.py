from machine import SPI,Pin,I2C
import time
import gt20l #导入库
import ssd1306

cs=Pin(15,Pin.OUT) #定义cs引脚
spi=SPI(-1,mosi=Pin(13),miso=Pin(12),sck=Pin(14)) #定义spi对象
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
gt20l=gt20l.gt20l(spi,cs) #定义gt20l对象
lcd=ssd1306.SSD1306_I2C(128,64,i2c)

data=gt20l.get_57ascll('C') #获取C的5x7ascll字体的点阵数据
data=list(map(lambda x:bin(int(x,16)).replace('0b',''),data))
data=list(map(lambda x:'0'*(8-len(x))+x,data))

print(data)
for x in range(8):
  for y in range(8):
    if int(data[x][7-y]):
      lcd.pixel(x,y,1)
lcd.show()




