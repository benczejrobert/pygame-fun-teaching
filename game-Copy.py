import sys, pygame

pygame.init()

blocks=64
sw=16*blocks
sh=8*blocks

up=0
down=sh
left=0
right=sw

screen = pygame.display.set_mode((sw,sh))


#title
pygame.display.set_caption('Clockworks game')

#fps
fps = 60

#gameobj class

class objec(pygame.sprite.Sprite):
    
    #init (poz, dimens :width, height)

    def __init__(self, xi=50, yi=50, w=blocks, h=blocks, movable = False, title = 'blackball.png', group = None):
        super (objec, self).__init__()
        
        self.image = pygame.image.load(title)
        pygame.transform.scale(self.image, (w,h))

        self.rect = self.image.get_rect()
        self.x=xi
        self.y=yi
        self.w=w
        self.h=h
        self.movable = movable

        self.oldx=self.x
        self.oldy=self.y

        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        if group != None:
            group.add(self)

    def move (self,event = None):

        if(self.movable ==True):

            
            if event.type == pygame.KEYDOWN:
                self.oldx=self.x
                self.oldy=self.y
                if event.key==pygame.K_DOWN and self.y+self.h<down:
                    pygame.draw.rect(screen, (0,0,0), [self.x,self.y,self.w,self.h])
                    self.y+=self.h
                if event.key==pygame.K_UP and self.y>0:
                    pygame.draw.rect(screen, (0,0,0), [self.x,self.y,self.w,self.h])
                    self.y-=self.h
                if event.key==pygame.K_LEFT and self.x>0:
                    pygame.draw.rect(screen, (0,0,0), [self.x,self.y,self.w,self.h])
                    self.x-=self.w
                if event.key==pygame.K_RIGHT and self.x+self.w<right:
                    pygame.draw.rect(screen, (0,0,0), [self.x,self.y,self.w,self.h])
                    self.x+=self.w

        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)

    def collide (self, spriteGroup):
        if pygame.sprite.spritecollide(self,spriteGroup, False):
            self.x=self.oldx
            self.y=self.oldy
            self.rect=pygame.Rect(self.x,self.y,self.w,self.h)


clock=pygame.time.Clock()
clock.tick(fps)

#group
objec_group = pygame.sprite.Group()
endgroup=pygame.sprite.Group()


b=objec(2*blocks,2*blocks,blocks,blocks,True,'blackball.png', objec_group)
# b.__init__(2*blocks,2*blocks,blocks,blocks,True,'blackball.png')
s=objec(0*blocks,0*blocks,blocks,blocks,True,'shinyball.png', objec_group)
# s.__init__(0*blocks,0*blocks,blocks,blocks,True,'shinyball.png')

# blackball end
be=objec(1*blocks,1*blocks,blocks,blocks,False,'blackball-ep.png', endgroup)
# be.__init__(1*blocks,1*blocks,blocks,blocks,False,'blackball-ep.png')

#shinyball end
se=objec(0*blocks,2*blocks,blocks,blocks,False,'shinyball-ep.png', endgroup)
# se.__init__(0*blocks,2*blocks,blocks,blocks,False,'shinyball-ep.png')

obs1=objec(0*blocks,1*blocks,blocks,blocks,False,'obs.png', objec_group)
# obs1.__init__(0*blocks,1*blocks,blocks,blocks,False,'obs.png')
obs2=objec(1*blocks,2*blocks,blocks,blocks,False,'obs.png', objec_group)
# obs2.__init__(1*blocks,2*blocks,blocks,blocks,False,'obs.png')
obs3=objec(3*blocks,2*blocks,blocks,blocks,False,'obs.png', objec_group)
# obs3.__init__(3*blocks,2*blocks,blocks,blocks,False,'obs.png')
obs4=objec(5*blocks,2*blocks,blocks,blocks,False,'obs.png', objec_group)
win=objec(0,0,sw,sh, False, 'win.png')
# win.__init__(0,0,sw,sh, False, 'win.png')


# objec_group.add(b,s,obs1,obs2)
# objec_group.add(obs3)
# objec_group.add(obs4)



# endgroup.add(se,be)
endgroup.draw(screen)

objec_group.draw(screen)

wingroup=pygame.sprite.Group()


gameexit = False

while not gameexit:
    pygame.display.update()
    endgroup.draw(screen)
    objec_group.draw(screen)
    wingroup.draw(screen)

    #movement
    for event in pygame.event.get():
        
        if ( event.type == pygame.KEYDOWN):
            b.move(event)
            s.move(event)
            for o in objec_group:
                objec_group.remove(o)
                o.collide(objec_group)
                objec_group.add(o)

            
            if (event.key == pygame.K_ESCAPE):
                gameexit = True

    if(b.x==be.x) and (b.y==be.y) and (s.x==se.x) and (s.y==se.y):
        wingroup.add(win)

                
    pygame.display.update()

    

pygame.quit()
sys.exit()
quit()



#poveste ->


