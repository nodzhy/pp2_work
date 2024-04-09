import pygame
import random
import sys
import time

pygame.init()

WIDTH = 400
HEIGHT = 600

speed = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

BACKGROUND = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 8/zher.png")
bad_screen = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 8/bad_screen.png")
bad_screen = pygame.transform.scale(bad_screen, (400, 600))

font = pygame.font.Font(None, 36)  # Установите шрифт и размер для текста

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 8/cosmos.png")
        self.image = pygame.transform.scale(self.image, (60, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-7, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(7, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 8/bsd.png")
        self.image = pygame.transform.scale(self.image, (40, 90))  # Изменение размера изображения
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)  # Рандомная координата x и фиксированная координата y

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, 1+speed)
        else:
            self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)  # Рандомная координата x и фиксированная координата y\

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 8/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Изменение размера изображения
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)  # Рандомная координата x и фиксированная координата y

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, 5)
        else:
            self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)  # Рандомная координата x и фиксированная координата y

class Crystal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Admin/Desktop/labs/week1/week 9/кристал.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Изменение размера изображения
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)  # Рандомная координата x и фиксированная координата y

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, 2)
        else:
            self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)  # Рандомная координата x и фиксированная координата y

enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
crystals = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
E1 = Enemy()
A1 = Coin()
B1 = Crystal()

enemies.add(E1)
coins.add(A1)
crystals.add(B1)
all_sprites.add(P1, E1, A1, B1)
done = False
cnt = 0

FPS = 60

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        screen.blit(bad_screen, (0, 0))
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        sys.exit()
    
    if pygame.sprite.spritecollideany(P1, coins):
        cnt += 1
        speed += 0.25
        coin = pygame.sprite.spritecollide(P1, coins, True)  # Получить список монет, с которыми столкнулся игрок и удалить их
        coin[0].kill()  # Удалить первую монетку из списка
        A1 = Coin()  # Добавить новую монетку в группу монеток
        coins.add(A1)
        all_sprites.add(A1)

    if pygame.sprite.spritecollideany(P1, crystals):
        cnt += 2
        speed += 0.5
        crystal = pygame.sprite.spritecollide(P1, crystals, True)  # Получить список кристаллов, с которыми столкнулся игрок и удалить их
        crystal[0].kill()  # Удалить первый кристалл из списка
        B1 = Crystal()  # Создать новый кристалл
        crystals.add(B1)  # Добавить новый кристалл в группу кристаллов
        all_sprites.add(B1)  # Добавить новый кристалл в общую группу спрайтов

    text_surface = font.render(f'POINT: {cnt}', True, colorRED)  # Создание текстовой поверхности
    screen.blit(text_surface, (250, 10))  # Отображение текстовой поверхности на экране

    pygame.display.flip()
    clock.tick(FPS)