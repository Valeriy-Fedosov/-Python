import pygame
import time
import random
import sys

pygame.init()

FPS = 15

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_w = 800
dis_h = 600

dis = pygame.display.set_mode((dis_w, dis_h))
pygame.display.set_caption('Игра змейка')

clock = pygame.time.Clock()

block = 10
speed = 5

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Набрано очков: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], block, block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_w / 6, dis_h / 3])

def draw_text(surface, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def input_screen():
    username = ""
    input_active = True
    while input_active:
        dis.fill(blue)
        draw_text(dis, "Введите ваш никнейм и нажмите ENTER", 25, white, 100, 100)
        draw_text(dis, "Цель игры: собрать больше яблок", 25, white, 100, 150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

        pygame.display.flip()
        clock.tick(FPS)

    return username

def gameLoop():
    username = input_screen ()

    game_over = False
    game_close = False

    x1 = dis_w / 2
    y1 = dis_h / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_w - block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_h - block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Вы проиграли! Нажмите C для продолжения игры или Q для выхода из нее", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change, y1_change = -block, 0
                elif event.key == pygame.K_RIGHT:
                    x1_change, y1_change = block, 0
                elif event.key == pygame.K_UP:
                    x1_change. y1_change = 0, -block
                elif event.key == pygame.K_DOWN:
                    x1_change. y1_change = 0, block

        if x1 >= dis_w or x1 < 0 or y1 >= dis_h or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, block, block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_w - block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_h - block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()