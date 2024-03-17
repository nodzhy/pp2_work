import pygame
from datetime import datetime
pygame.init()
done=False
L, H = 1200, 800
screen = pygame.display.set_mode((L, H))

clock_img = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 7/mainclock.png")
minute_img = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 7/rightarm.png")
second_img = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 7/leftarm.png")

clock_place = clock_img.get_rect(center=(L/2, H/2))
minute_place = minute_img.get_rect(center=(L/2, H/2))
second_place = second_img.get_rect(center=(L/2, H/2))

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill((255, 255, 255))
    screen.blit(clock_img, clock_place)

    now = datetime.now()
    current_time = now.time()
    current_minute = current_time.minute
    current_second = current_time.second

    minute_angle = (current_minute * 6)-36
    second_angle = (current_second * 6)+3

    rotated_minute_hand = pygame.transform.rotate(minute_img, -minute_angle)
    rotated_second_hand = pygame.transform.rotate(second_img, -second_angle)

    screen.blit(rotated_minute_hand, rotated_minute_hand.get_rect(center=minute_place.center))
    screen.blit(rotated_second_hand, rotated_second_hand.get_rect(center=second_place.center))

    pygame.display.flip()
    clock.tick(60)