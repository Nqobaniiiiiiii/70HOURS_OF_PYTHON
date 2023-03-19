  
import pygame
import time
import math
from utilis import scale_image, blit_rotate_centre
import sys

    
try :
    GRASS = scale_image(pygame.image.load("images/grass.jpeg") ,2.5)
    FINISH = pygame.image.load("images/finish.jpeg")
    FINISH_MASK = pygame.mask.from_surface(FINISH)
    FINISH_POSITION = (130, 250)
    GREEN_CAR = scale_image(pygame.image.load("images/grey-car.jpeg"),0.5)

    GREY_CAR = scale_image(pygame.image.load("images/grey-car.jpeg"),0.5)
    PURPLE_CAR = pygame.image.load(("images/purple-car.jpeg"),0.5)
    RED_CAR = pygame.image.load(("images/red-car.jpeg"),0.5)

    TRACK_BORDER = scale_image(pygame.image.load("images/track-border.jpeg"), 0.9)
    TRACK = scale_image(pygame.image.load("images/track.jpeg"),0.9)
    TRACK_BORDER_MASK =pygame.mask.from_surface(TRACK_BORDER)
    WHITE_CAR =scale_image(pygame.image.load("images/white-car.jpeg"),0.5)

except FileNotFoundError: 
       print('The file is no            t present.')

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")


FPS = 60

PATH = [(175, 119), (110,70), (56,133),(70, 481),(318,731),(404,680),(418, 521),(507, 475),(600, 551),(613,715),(736,713),
       (734,399), (611,357) , (409,343) ,(433, 257), (697, 258) ,(738,123),(581,71),(303, 78),(275,377),(176,388),(178,260)]


class AbstractCar:
    
    
    def __init__(self, max_vel, rotation_vel):
       self.img = self.IMG
       self.max_vel = max_vel
       self.vel = 0
       self.rotation_vel = rotation_vel
       self.angle = 0
       self.x, self.y = self.START_POS
       self.acceleration = 0.5
    
       
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right: 
            self.angle -= self.rotation_vel
            
    def draw(self,win):  
            blit_rotate_centre(win, self.img, (self.x, self.y), self.angle) 
        
    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()
        
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians)*self.vel
        horizontal = math.sin(radians)*self.vel
        
        self.y -= vertical
        self.x -= horizontal
        
    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()
    
    def collide(self, mask, x=0 , y=0) :
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi
    
    def reset(self):
        self.x, self.y = self. START_POS
        self.angle = 0
        self.vel = 0


        
class PlayerCar(AbstractCar):  
    
    IMG = RED_CAR
    START_POS = (180, 200)
             
    def bounce(self) :
     self.vel = -self.vel
     self.move()
     
    def reduce_speed(self) :
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()
    
    
class ComputerCar (AbstractCar):
    IMG = GREEN_CAR
    START_POS = (150,200)
    
def draw(win, images, player_car):
     for img, pos in images:
        win.blit(img, pos)
        
     player_car.draw(win)
     pygame.display.update()     
     

     
def move_player(player_car):
    keys= pygame.key.get_pressed()
    moved = False
    
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()
        
       
    if not moved:
       player_car.reduce_speed()

run = True 
clock = pygame.time.Clock()
images= [(GRASS,(0, 0)), (TRACK,(0, 0)),(FINISH,FINISH_POSITION),(TRACK_BORDER, (0, 0))]
player_car = PlayerCar(8, 8)
 
while run:
    clock.tick(FPS)
    
    draw(WIN, images, player_car)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
        
    move_player(player_car)

    if player_car.collide(TRACK_BORDER_MASK) != None :
       player_car.bounce()
        
    finish_poi_collide = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_poi_collide !=None:
            if finish_poi_collide[1] == 0:
                player_car.bounce()
                 
            else:
                player_car.reset()
                print("FINISH ")

    
pygame.quit()

