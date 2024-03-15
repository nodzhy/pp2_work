import pygame
pygame.init() 
screen= pygame.display.set_mode((1200, 700))
red=(255, 0, 0)
white=(255, 255, 255)
done=False
x=600
y=350
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
 
    keys= pygame.key.get_pressed() 

    if keys[pygame.K_RIGHT] and x<1200:
        x+=1

    if keys[pygame.K_LEFT] and x>0:
        x-=1

    if keys[pygame.K_DOWN] and y<700:
        y+=1

    if keys[pygame.K_UP] and y>0:
        y-=1

    screen.fill((white))

    pygame.draw.circle(screen, red, (x, y), 25)

    pygame.display.flip()

    clock.tick(400)

