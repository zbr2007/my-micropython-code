from machine import SPI,Pin
import time
import gt20l #导入库

cs=Pin(15,Pin.OUT) #定义cs引脚
spi=SPI(-1,mosi=Pin(13),miso=Pin(12),sck=Pin(14)) #定义spi对象

gt20l=gt20l.gt20l(spi,cs) #定义gt20l对象
print(gt20l.get_gb2312_font([0xd6,0xd0])) #0xd6是"中"在gb2312编码中高八位，0xd0是低八位
