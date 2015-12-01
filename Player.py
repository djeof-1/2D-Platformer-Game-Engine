import pygame

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 32
        self.width = 32
        self.velocity=0
        self.falling = True
        self.onGround = False
        
    def jump(self):
        if (self.onGround == False):
            return
        else:
            self.velocity = 30
            self.onGround = False
        
    def detectCollisions(self, x1,y1,w1,h1,x2,y2,w2,h2):
       
        if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
            return True,1

        elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
            return True,1
                    
        elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
            return True,1

        elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
            return True
        
        else:
            return False

        
    def update(self,gravity, blockList):
        if (self.velocity < 0):
            self.falling = True
        
        hasCollided = False
        
        blockX,blockY=0,0
        
        for block in blockList:
            hasCollided = self.detectCollisions(self.x, self.y, self.width, self.height, block.x, block.y, block.width, block.height)
            if (hasCollided):
                blockX = block.x
                blockY = block.y
                break
        if (hasCollided):
            if (self.falling == True):
                self.y = blockY - self.height
                self.falling = False
                self.onGround = True
                self.velocity = 0
        else:
            self.falling = True
            self.onGround = False

        if (self.onGround == False):
            self.velocity+=gravity
        self.y-=self.velocity

    def render(self,window):
        #img = pygame.image.load('Sprites/megaman.bmp')
        pygame.draw.rect(window, (0,0,0),(self.x, self.y, self.width, self.height))
        #window.blit(img, (self.x, self.y))

