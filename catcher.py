import pygame
import sys
from random import randint
#pylint: disable=no-mumber

pygame.init()

score = 0
total = 0

myfont = pygame.font.SysFont('monospace', 30)
background_image =  pygame.image.load(r'C:\Users\User\Desktop\Python\ball\images\background.jpg')
gameover_image = pygame.image.load(r'C:\Users\User\Desktop\Python\ball\images\game_over.jpg')
winner_image = pygame.image.load(r'C:\Users\User\Desktop\Python\ball\images\congr1.jpg')

# Making dictionaries with settings for everything.

display = {
    "width": 800,
    "height": 600
}

paddle = {
    "width": 150,
    "height": 30,
    "x": 300,
    "y": 560,
    "velocity": 20
}

ball = {
    "radius": 15,
    "y": 30,
    "x": randint(20, display["width"] - 10),
    "velocity": 15
}
ball1 = {
    "radius": 10,
    "y": 30,
    "x": randint(0, display["width"] - 10),
    "velocity": 10
}

screen  = pygame.display.set_mode((display["width"], display["height"]))

game_over = False 
def Gameover():
    screen.blit(gameover_image, (0,0))
    pygame.display.flip()
    pygame.quit()
    #sys.exit()

winner = False 
def Winner():
    screen.blit(winner_image, (0,0))
    pygame.display.flip()
    pygame.quit()
    #sys.exit()

done = False 
while  not done :
    # чтобы наш цикл не повторялось слишком быстро
    pygame.time.delay(100)
    #цвет экрана
    screen.fill((0, 0, 255))
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #moving
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle["x"] -= paddle["velocity"]

    if keys[pygame.K_RIGHT]:
        paddle["x"] += paddle["velocity"]
    #collosion
    if ball["y"] + ball["radius"] >= paddle["y"]:
        if ball["x"] > paddle["x"] and ball["x"] < paddle["x"] + paddle["width"]:
            score += 1
        total += 1
        ball["y"] = ball["radius"]
        ball["x"] = randint(0, display["width"])
    if ball1["y"] + ball1["radius"] >= paddle["y"]:
        if ball1["x"] > paddle["x"] and ball1["x"] < paddle["x"] + paddle["width"]:
            score += 1
        total += 1
        ball1["y"] = ball1["radius"]
        ball1["x"] = randint(0, display["width"])
   
   
    
    if total == 6:
        if score == 6:
            Winner()
        else:
            Gameover()

    ball["y"] += ball["velocity"]
    ball1["y"] += ball1["velocity"]
    
    
    screen.blit(background_image, (0,0))

    
    pygame.draw.circle(screen, (255,0 , 0), (ball["x"], ball["y"]),   ball["radius"])
    pygame.draw.circle(screen, (255,0 , 0), (ball1["x"], ball1["y"]), ball1["radius"])
    pygame.draw.rect(screen, (0, 0, 0), (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))
    
    textsurface = myfont.render("score: {0}/{1}".format(score, total), False, (255, 255, 255))
    screen.blit(textsurface, (10, 10))

    
    pygame.display.flip()
pygame.quit()