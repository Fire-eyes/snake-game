import sys, pygame
import random
import math
pygame.init()

#Need to get Screen size*
WIDTH = 500
HEIGHT = 500
fps = 30
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#Defining mouse inputs as colours
RGBColors = {
    (False, False, False) : 'black',
    (True, False, False)  : 'red',
    (False, True, False)  : 'green',
    (False, False, True)  : 'blue',
    (True, True, False)  : 'yellow',
    (False, True, True)  : 'cyan',
    (True, False, True)  : 'magenta',
    (True, True, True)  : 'white',
}

#Start of apple stuff
AppleColors = ['red', 'yellow', 'green']
CurrentApple = {
    "xPosition": WIDTH+20,
    "yPosition": HEIGHT+20,
    "Colour": 'red'
}
def SpawnApple():
    print()
    CurrentApple.update({"xPosition": random.randrange(0, WIDTH)})
    CurrentApple.update({"yPosition": random.randrange(0, HEIGHT)})
    CurrentApple.update({"Colour": random.choice(AppleColors)})

#Start the apple spawns
SpawnApple()

score = 0
#Game Loop
run = True
while run:
    screen.fill('slategrey')
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Button Inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                SpawnApple()
                print(CurrentApple)
                print("Apple Spawn")

    #Mouse movement
    cursorColor = RGBColors[pygame.mouse.get_pressed()]
    mouse_Position = pygame.mouse.get_pos()
    pygame.draw.circle(screen, cursorColor, mouse_Position, 10)

    #Redraws the apple
    pygame.draw.circle(screen, CurrentApple["Colour"], (CurrentApple["xPosition"], CurrentApple["yPosition"]), 5)

    #Snake Overlaps w/ Apple
    xDistance = abs(mouse_Position[0] - CurrentApple["xPosition"])
    yDistance = abs(mouse_Position[1] - CurrentApple["yPosition"])
    #Math: a^2 + b^2 = c^2
    distance = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))
    if distance <= 15:
        #If colours are the same
        if str(CurrentApple["Colour"]) == str(cursorColor):
            score += 1
            print(score)
            #Moves apple
            SpawnApple()
    

    #Debuging Stuff
    #print(mouse_Position)
    #print(pygame.mouse.get_pressed())

    pygame.display.flip()
pygame.quit()