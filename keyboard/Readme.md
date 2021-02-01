这是由每天new亿个对象开发的基于ssd1306的micropython键盘显示库
自以为大有所益

使用方法:
1.创建键盘对象:keyboard.keyboard(oled)
例子:
import ssd1306
import keyboard
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled=ssd1306.SSD1306_I2C(128,64,i2c)
k=keyboard.keyboard(oled) #初始化键盘对象,要带上ssd1306对象

2.显示键盘:init(title='')
例子：
import ssd1306
import keyboard
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled=ssd1306.SSD1306_I2C(128,64,i2c)
k=keyboard.keyboard(oled) #初始化键盘对象,要带上ssd1306对象
k.init('title') #初始化，显示键盘，标题是'title'

或者不带标题:
import ssd1306
import keyboard
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled=ssd1306.SSD1306_I2C(128,64,i2c)
k=keyboard.keyboard(oled) #初始化键盘对象,要带上ssd1306对象
k.init() #初始化，显示键盘，无标题

3.常用函数:
moveUp():上移
moveDown():下移
moveLeft():左移
moveRight():右移
get():返回选定的字符
ent(title):设定标题区文字(保留后面12位)
clear_ent():清空标题区，包括下面的横线
goto([x,y]):直接移动至某位置

4.基本没什么用的不常用函数:
update():强制刷新键盘,内部调用的，用户拿来基本上没什么用
clear():内部调用的,用户拿来基本上没什么用

5.数据位置:
zb:目前选中坐标

6.说明:
考虑各种原因，库中不会自动更新屏幕，可以调用ssd1306的show函数更新

本源码开源，欢迎修改，更欢迎把改好的源码发回给我awa，有bug我会尽快修复
严禁倒卖
作者qq:2517889752

会更新，敬请关注