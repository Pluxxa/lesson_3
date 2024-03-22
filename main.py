import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("C:/PyCh/project1/English-Words/lesson_3/img/AK-47.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("C:/PyCh/project1/English-Words/lesson_3/img/target.png")
target_width = 50
target_height = 50

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Шрифт для отображения текста
font = pygame.font.SysFont(None, 36)

def show_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 5
                elif event.key == pygame.K_2:
                    return 10
                elif event.key == pygame.K_3:
                    return 15
        screen.fill((0, 0, 0))
        text = font.render("Нажмите 1, 2 или 3 для выбора попыток (5, 10, 15)", True, (255, 255, 255))
        screen.blit(text, (100, SCREEN_HEIGHT // 2))
        pygame.display.update()

attempts = show_menu()

hits = 0
misses = 0
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
start_time = pygame.time.get_ticks()
TIME_LIMIT = 5000  # 5 секунд

running = True
while running:
    screen.fill(color)
    current_time = pygame.time.get_ticks()
    if current_time - start_time >= TIME_LIMIT:
        misses += 1
        start_time = pygame.time.get_ticks()  # Сброс таймера
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and attempts > 0:
            attempts -= 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
            else:
                misses += 1
            start_time = pygame.time.get_ticks()  # Сброс таймера
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))
    hit_text = font.render(f'Попаданий: {hits}', True, (255, 255, 255))
    miss_text = font.render(f'Промахов: {misses}', True, (255, 255, 255))
    attempts_text = font.render(f'Осталось попыток: {attempts}', True, (255, 255, 255))
    screen.blit(hit_text, (10, 10))
    screen.blit(miss_text, (10, 50))
    screen.blit(attempts_text, (10, 90))

    if attempts <= 0:
        running = False
        # Отображаем окончательный счет после окончания игры
        screen.fill((0, 0, 0))
        final_hits_text = font.render(f'Итоговое количество попаданий: {hits}', True, (255, 255, 255))
        final_misses_text = font.render(f'Итоговое количество промахов: {misses}', True, (255, 255, 255))
        screen.blit(final_hits_text, (100, SCREEN_HEIGHT // 2 - 20))
        screen.blit(final_misses_text, (100, SCREEN_HEIGHT // 2 + 10))
        pygame.display.update()
        # Даем пользователю время увидеть итоговый счет
        pygame.time.wait(5000)

    pygame.display.update()
