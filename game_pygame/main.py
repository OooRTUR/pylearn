import sys, pygame
from random import randrange

class CellContainer:
    position = [0,0]
    cells = []
    cellSize = 50
    cellDistance = 5
    size =[0,0]

    def __init__(self, position,size):
        print("self container")
        self.position = position
        self.size = size
        for x in range(size[0]):
            self.cells.append([])
            for y in range(size[1]):
                color = (randrange(255),randrange(255), randrange(255))
                newCell = Cell1(color,self.cellSize, self.cellSize)
                self.cells[x].append(newCell)
                

    def Draw(self, screen):
        for x in range(len(self.cells[0])):
            for y in range(len(self.cells[1])):
                xPos = self.position[0] + x*self.cellSize + self.cellDistance * x
                yPos = self.position[1] + y*self.cellSize + self.cellDistance * y
                # pygame.draw.rect(screen, self.cells[x][y].color,(xPos,yPos,self.cellSize,self.cellSize))
                self.cells[x][y].Draw(screen)


class Cell1(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def Draw(self, screen):
        screen.blit(self.image, self.image.get_rect())

pygame.init()
cellContainer = CellContainer((0,0),(5,5))

size = width, height = 640, 480
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()


cell1 = Cell1((0,0,255),30,30)
cellRect = cell1.image.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(cell1.image, cell1.image.get_rect())
    # cellContainer.Draw(screen)
    pygame.display.flip()

    pygame.time.delay(100)

