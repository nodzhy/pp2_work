import pygame
pygame.init()
done = False
paused = False
L, H = 700, 500
screen = pygame.display.set_mode((L, H))

player_png = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 7/ih.png")

music1 = pygame.mixer.Sound("C:/Users/Admin/Desktop/labs/week1/week 7/Голая.mp3")
music2 = pygame.mixer.Sound("C:/Users/Admin/Desktop/labs/week1/week 7/Романс.mp3")
music3 = pygame.mixer.Sound("C:/Users/Admin/Desktop/labs/week1/week 7/Seven.mp3")
music4 = pygame.mixer.Sound("C:/Users/Admin/Desktop/labs/week1/week 7/Любите Девушки.mp3")

music_list = [music1, music3, music2, music4]

player_place = player_png.get_rect(center=(L/2, H/2))

current_music_index = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        music_list[current_music_index].stop()
        current_music_index += 1
        if current_music_index == len(music_list):
            current_music_index = 0
        music_list[current_music_index].play()
    
    elif keys[pygame.K_LEFT]:
        music_list[current_music_index].stop()
        current_music_index -= 1
        if current_music_index == -1:
            current_music_index = len(music_list) - 1
        music_list[current_music_index].play()

    elif keys[pygame.K_SPACE]:
        if not paused:
            pygame.mixer.pause()
            paused = True
        else:
            pygame.mixer.unpause()
            paused = False

    else:
        music_list[current_music_index].play()

    screen.fill((255, 255, 255))
    screen.blit(player_png, player_place)

    pygame.display.flip()
