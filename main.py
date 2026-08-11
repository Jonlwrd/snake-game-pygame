# initial settings 
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game Python")
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0, 0)
green = (0, 255, 0)

# snake parameters 
size_square = 20 
game_speed = 7

def generate_food():
     food_x = round(random.randrange(0, width - size_square) / 20.0) * 20.0
     food_y = round(random.randrange(0, height - size_square) / 20.0) * 20.0
     return food_x, food_y 

def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, red, [food_x, food_y, size, size])

def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, green, [pixel[0], pixel[1], size,size])

def draw_points(points):
    source = pygame.font.SysFont("Arial", 50)
    text = source.render(f"Points: {str(points)}", True, white)
    screen.blit(text, [10, 10])

def select_speed(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = size_square
    if key == pygame.K_UP:
        speed_x = 0
        speed_y = -size_square
    if key == pygame.K_LEFT:
        speed_x = -size_square
        speed_y = 0
    if key == pygame.K_RIGHT:
        speed_x = size_square
        speed_y = 0      
    return speed_x, speed_y 

def run_game():
    end_game = False 

    x = width / 2
    y =  height / 2

    speed_x = 0 
    speed_y = 0

    size_snake = 1
    pixels = []

    food_x, food_y = generate_food()

    while not end_game:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)

        # update snake position
        if x < 0 or x > width - size_square or y < 0 or y > height - size_square:
            end_game = True
        x += speed_x
        y += speed_y

        # collision correction
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        # draw snake
        pixels.append([x, y])
        if len(pixels) > size_snake:
            del pixels[0]


        # check if snake hit itself
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        


        draw_snake(size_square, pixels)


        draw_food(size_snake - 1, food_x, food_y)


        draw_food(size_square, food_x, food_y)

        draw_points(size_snake - 1)
        # screen update
        pygame.display.update()

        # create a new food if snake eat the food
        if x == food_x and y == food_y:
            size_snake += 1
            food_x, food_y = generate_food()


        clock.tick(game_speed)

 
run_game()