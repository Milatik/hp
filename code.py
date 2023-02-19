from pygame import *

display.set_caption("Моя первая игра")
window = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy_1.jpg'), (700, 500))
GREEN = (0,255,0)
class Card(sprite.Sprite):
    def _init_(self,width,height,x,y,color): 
        super()._init_()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)

class Pic(sprite.Sprite):
    def _init_(self,w,h,x,y): 
        super()._init_()
        self.image=transform.scale(image.load('Asset 8@4x.png'),(w, h))
        self.x = x
        self.y = y
    def reset(self):
        window.blit(self.image,(self.x,self.y))

player1 = Card(80,80,100,200,GREEN)
player2 = Pic(100,100,500,200)

run = True
while run:
    time.delay(50)
    window.blit(background,(0,0))
    player1.draw()
    player2.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()