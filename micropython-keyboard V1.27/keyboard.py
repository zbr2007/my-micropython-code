class keyboard:
  def __init__(self,lcd):
    self.lcd=lcd
    self.zb=[0,0]
    self.key=[('a','b','c','d','e'),('f','g','h','i','j'),('k','l','m','n','o'),('p','q','r','s','t'),('u','v','w','x','y'),('z','back','enter')]
  def init(self):
    self.lcd.fill(0)
    for xx in range(5):
      for x in range(5):
        self.lcd.rect(x*25,1+(xx*10),22,9,1)
        self.lcd.text(self.key[xx][x],6+(x*25),1+(xx*10))
    self.lcd.rect(0,51,22,9,1) #z
    self.lcd.rect(25,51,22,9,1) #back
    self.lcd.rect(50,51,22,9,1) #enter
    self.lcd.text(self.key[5][0],5,51)
    self.lcd.text('en',28,51)
    self.lcd.text('ba',53,51)
    
    self.lcd.fill_rect(0,1,22,9,1)
    self.lcd.text(self.key[0][0],6,1,0)
  def moveUp(self):
    if self.zb[1] != 0:
      self.clear()
      self.zb[1]-=1
      self.update()
  def moveDown(self):
    if self.zb[1] != 4 or self.zb[0]==0:
      if (self.zb[0] == 0 or self.zb[0] == 1 or self.zb[0] == 2) and self.zb[1] ==4:
        self.clear()
        self.zb[1]+=1 #移动到z代码
        self.update()
      elif self.zb[1] <=4:
        self.clear()
        self.zb[1]+=1 #正常下移
        self.update()
  def moveLeft(self):
    if self.zb[0] !=0:
      self.clear()
      self.zb[0]-=1 #左代码
      self.update()
  def moveRight(self):
    if self.zb[1] != 5 or (self.zb[1] == 5 and self.zb[0] !=2):
      if self.zb[0] !=4:
        self.clear()
        self.zb[0]+=1 #右代码
        self.update()
  def get(self):
    r=self.key[self.zb[1]][self.zb[0]]
    return r
  def clear(self):
    if self.zb[1] != 5 or (self.zb[0] == 0 and self.zb[1] == 5):
      self.lcd.fill_rect(self.zb[0]*25,1+(self.zb[1]*10),22,9,0) #清除
      self.lcd.rect(self.zb[0]*25,1+(self.zb[1]*10),22,9,1)
      self.lcd.text(self.key[self.zb[1]][self.zb[0]],6+(self.zb[0]*25),1+(self.zb[1]*10))
    elif self.zb[0] == 1:
      self.lcd.fill_rect(25,51,22,9,0) #清除
      self.lcd.rect(25,51,22,9,1)
      self.lcd.text('en',28,51,1)
    elif self.zb[0] == 2:
      self.lcd.fill_rect(50,51,22,9,0) #清除
      self.lcd.rect(50,51,22,9,1)
      self.lcd.text('ba',53,51,1)
  def update(self):
    if self.zb[1] != 5 or (self.zb[0] == 0 and self.zb[1] == 5):
      self.lcd.fill_rect(self.zb[0]*25,1+(self.zb[1]*10),22,9,1)
      self.lcd.text(self.key[self.zb[1]][self.zb[0]],6+(self.zb[0]*25),1+(self.zb[1]*10),0)
    elif self.zb[0] == 1:
      self.lcd.fill_rect(25,51,22,9,1)
      self.lcd.text('en',28,51,0)
    elif self.zb[0] == 2:
      self.lcd.fill_rect(50,51,22,9,1)
      self.lcd.text('ba',53,51,0)
  def goto(self,x,y):
    self.clear()
    self.zb=[x,y]
    self.update()
