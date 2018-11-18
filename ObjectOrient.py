import pygame
pygame.init()       #initialize pygame

win = pygame.display.set_mode((640, 359))   #create window of 500x500
pygame.display.set_caption("Donation Game")       #name the window to "string"

#Loading images
bg = pygame.image.load("background2.png")         #Background image
scaled_bg = pygame.transform.scale(bg, (640, 359))
charSprite = pygame.image.load("sprites.png")    #Sprites image
buttonUp = pygame.image.load("buttonup.png")     #Buttonup image
ScaledButUp = pygame.transform.scale(buttonUp, (75,75))
buttonDown = pygame.image.load("buttondown.png") #Buttondown image
ScaledButDown = pygame.transform.scale(buttonDown,(75,75))
monster01 = pygame.image.load("teostra.png")
monster01 = pygame.transform.scale(monster01,(1280,576))
player02 = pygame.image.load("player02.png")
player02 = pygame.transform.scale(player02,(1020,426))

#Create array of walking direction sprites
'''
walkRight = []
walkLeft = []
walkUp = []
walkDown = []
for i in range(3):
    walkRight.append(charSprite.subsurface(i*64,128,64,64))
    walkLeft.append(charSprite.subsurface(i*64,64,64,64))
    walkUp.append(charSprite.subsurface(i*64,192,64,64))
    walkDown.append(charSprite.subsurface(i*64,0,64,64))
'''

#Ingame clock
clock = pygame.time.Clock()
class monster():
    def __init__(self, x, y, width, height, level, monSprite, numSprites, numSpritesPerRow, numRows):
        #Geometry and physics
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #Idle loop variables
        self.idleCount = 0
        #Monster attributes
        self.level = level
        #Idle sprites animation
        self.sprites = []
        self.numSprites = numSprites
        spriteCount = 0
        for i in range(numSpritesPerRow):
            for j in range(numRows):
                self.sprites.append(monSprite.subsurface(i*self.width, j*self.height, self.width, self.height))
                spriteCount += 1
                if spriteCount == numSprites:
                    break

    def draw(self,win):
        # Cycling idle sprites
        if self.idleCount >= self.numSprites :
            self.idleCount = 0

        win.blit(self.sprites[self.idleCount],(self.x, self.y))

class player():
    def __init__(self, x, y, width, height):
        #Geometry and physics
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #Movespeed variables
        self.vel = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        #Character attributes
        self.exp = 0
        self.level = 1
        #Walking sprites animation
        self.walkRight = []
        self.walkLeft = []
        self.walkUp = []
        self.walkDown = []
        for i in range(3):
            self.walkRight.append(charSprite.subsurface(i * 64, 128, 64, 64))
            self.walkLeft.append(charSprite.subsurface(i * 64, 64, 64, 64))
            self.walkUp.append(charSprite.subsurface(i * 64, 192, 64, 64))
            self.walkDown.append(charSprite.subsurface(i * 64, 0, 64, 64))

    def draw(self, win):
        # Cycling walking sprites
        if self.walkCount + 1 >= 4:
            self.walkCount = 0
        # Call walking sprites
        if self.left:
            win.blit(self.walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            win.blit(self.walkUp[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            win.blit(self.walkDown[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(charSprite, (self.x, self.y), (64, 0, 64, 64))  # Default sprit into window (image, (position), (starting crop, end crop)

# Drawing character
def redrawGameWindow():     #Function of character update

    #Rookie test
    #win.fill((0, 0, 0))  # fill the window with black so that character doesnt duplicate
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # Character as a rectangle (placed in window, colour of rectangle, position and size)

    #Putting images in window
    win.blit(scaled_bg, (0, 0))  #Background
    win.blit(ScaledButUp, (300, 150)) #Buttonup
    #pygame.draw.AAfilledRoundedRect(win, (10, 10, 100, 100), (255, 255, 255),  0.5)
    man.draw(win)
    teostra.draw(win)

    #Hold mouse down to click button
    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.rect(win, (0, 0, 0), (10, 10, 100, 100))
        win.blit(ScaledButDown, (300, 150))

    #Experience bar
    pygame.draw.rect(win, (255, 255, 25), (man.x+9, man.y-11, 50, 10))      #draw rectangle, (in window, colour, position, size)
    pygame.draw.rect(win, (179, 149, 0),  (man.x+9, man.y-11, 50, 10))

    #Level counter
    text = font.render('Lv. ' + str(man.level), 1, (0, 0, 0))
    win.blit(text, (man.x+9, man.y-13))

    pygame.display.update()  # Update game

# Main loop


man = player(50, 50, 64, 64)
teostra = monster(350, 100, 256, 192, 1, monster01, 14, 5, 3)
font = pygame.font.SysFont('Arial', 12, True)   #Define font type, size, bold, italics
run = True
while run:
    #pygame.time.delay(100)  #ingame clock, in milliseconds
    clock.tick(10)

    #Monster idle loop
    teostra.idleCount += 1

    #Checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()    #create list of keys, origin in top left corner

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        man.x += man.vel
        man.left = False
        man.right = True
        man.up = False
        man.down = False
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        man.y += man.vel
        man.left = False
        man.right = False
        man.up = False
        man.down = True
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        man.y -= man.vel
        man.left = False
        man.right = False
        man.up = True
        man.down = False

    else:
        man.walkCount = 1
        '''
        man.right = False
        man.left = False
        man.up = False
        man.down = False
        '''


    redrawGameWindow()  #Call func for character update


pygame.quit()