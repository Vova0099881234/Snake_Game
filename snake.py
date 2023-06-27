import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (51, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (0, 102, 0)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == 0:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        else:
            segment_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            pygame.draw.rect(dis, segment_color, [x[0], x[1], snake_block, snake_block])


def message1(msg, color):
    font_size = 80
    font = pygame.font.Font(None, font_size)
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 4, dis_height / 3])


def message(msg, color):
    font_size = 27
    font = pygame.font.Font(None, font_size)
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3.8, dis_height / 2.1])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    food_list = []
    num_foods = 5

    for _ in range(num_foods):
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        food_list.append([foodx, foody])

    while not game_over:

        while game_close:
            dis.fill(red)
            message1("GAME OVER!", white)
            message("Press ENTER-Play Again or ESC-Quit", white)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        for food in food_list:
            food_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            pygame.draw.rect(dis, food_color, [food[0], food[1], snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        for i, food in enumerate(food_list):
            if x1 == food[0] and y1 == food[1]:
                food_list[i] = [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
                                round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0]
                Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
