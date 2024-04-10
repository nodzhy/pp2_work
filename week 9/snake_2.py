import pygame
import time
import random

# Настройки игры
snake_speed = 15
window_width = 720
window_height = 480

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Инициализация Pygame
pygame.init()
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_width, window_height))
fps = pygame.time.Clock()

# Позиция и начальное тело змеи
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Позиции фруктов и больших фруктов
fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]
big_fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]

# Флаги появления фруктов и больших фруктов
fruit_spawn = True
big_fruit_spawn = True

# Направление змеи с самого начала
direction = 'RIGHT'
change_to = direction

# Счет
score = 0

# Таймер для большого фрукта
big_fruit_timer = 0
fruit_change_interval = 500  

# Отображение счета
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Счет : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect) 

# Отображение времени большого фрукта
def show_time(choice, color, font, size):
    time_font = pygame.font.SysFont(font, size)
    time_surface = time_font.render("time: "+str(big_fruit_timer) + "/500", True, color)
    time_rect = time_surface.get_rect()
    #место где будет стоять счетчик
    time_rect.topright = (window_width - 10, 1)
    game_window.blit(time_surface, time_rect)

# Завершение игры
def game_over():
    game_over_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = game_over_font.render('Loser, you have only: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_width / 2, window_height / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Избегаем двойного изменения направленияe
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Перемещение змеи
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Обновление таймера для большого фрукта
    big_fruit_timer += fps.get_rawtime()

    # Если прошло больше 5 секунд, меняем положение большого фрукта и сбрасываем таймер
    if big_fruit_timer > fruit_change_interval:
        big_fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]
        big_fruit_timer = 0

    # Проверка столкновений змеи
    if snake_position[0] < 0 or snake_position[0] > window_width - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_height - 10:
        game_over()

    # Проверка столкновения с собственным телом
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Перемещение тела змеи и проверка съедания фруктов
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]

    # Проверка съедания большого фрукта
    snake_head_rect = pygame.Rect(snake_position[0], snake_position[1], 10, 10)
    big_fruit_rect = pygame.Rect(big_fruit_position[0], big_fruit_position[1], 15, 15)
    snake_body.insert(0, list(snake_position))
    if snake_head_rect.colliderect(big_fruit_rect):
        score += 15
        big_fruit_spawn = False
        big_fruit_timer = 0
    else:
        snake_body.pop()

    if not big_fruit_spawn:
        big_fruit_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]

    fruit_spawn = True
    big_fruit_spawn = True

    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(big_fruit_position[0], big_fruit_position[1], 20, 20))

    # Отображение счета
    show_score(1, white, 'times new roman', 20)

    show_time(1, red, 'times new roman', 20)

    # Обновление экрана
    pygame.display.update()

    # Частота обновления кадров
    fps.tick(snake_speed)