from machine import SPI,Pin,I2C
import gt20l #导入库
import ssd1306
import time

cs=Pin(15,Pin.OUT) #定义cs引脚
spi=SPI(-1,mosi=Pin(13),miso=Pin(12),sck=Pin(14)) #定义spi对象
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
gt20l=gt20l.gt20l(spi,cs) #定义gt20l对象
lcd=ssd1306.SSD1306_I2C(128,64,i2c)

all_gb=((0xb0,0xa1),(0xd5,0xe2),(0xd5,0xe2),(0xba,0xcb),(0xc0,0xef),(0xc2,0xf0)) #gb2312编码列表，分别对应"啊","这","这","核","里","吗"
off_set=0
for x in range(2):
  data=gt20l.get_gb2312_font(all_gb[x])
  data=list(map(lambda x:bin(int(x,16)).replace('0b',''),data))
  data=list(map(lambda x:'0'*(8-len(x))+x,data))

  data1=data[0:15]
  data2=data[16:31]

  t1=time.time()
  for x in range(15):
    for y in range(8):
      if int(data1[x][7-y]):
        lcd.pixel(off_set*16+x,y,1)
  for x in range(15):
    for y in range(8):
      if int(data2[x][7-y]):
        lcd.pixel(off_set*16+x,y+8,1)
  lcd.show()
  off_set+=1
off_set=0
for x in range(4):
  data=gt20l.get_gb2312_font(all_gb[x+2])
  data=list(map(lambda x:bin(int(x,16)).replace('0b',''),data))
  data=list(map(lambda x:'0'*(8-len(x))+x,data))

  data1=data[0:15]
  data2=data[16:31]

  t1=time.time()
  for x in range(15):
    for y in range(8):
      if int(data1[x][7-y]):
        lcd.pixel(off_set*16+x,16+y,1)
  for x in range(15):
    for y in range(8):
      if int(data2[x][7-y]):
        lcd.pixel(off_set*16+x,16+y+8,1)
  lcd.show()
  off_set+=1
