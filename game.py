import pygame
import os

WIDTH, HEIGHT = 900, 500
BACKGROUND_COLOUR = (0, 153, 255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55 , 40
FPS = 60
x_velocity = 5
y_velocity = 3
border = pygame.Rect


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP =pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90 )
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP =pygame.transform.rotate( pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270 )

pygame.display.set_caption("Space Shooters!")

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            # Quit event
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        draw_window(red, yellow)
    pygame.quit()



# Sets background colour to light blue
def draw_window(red, yellow):
    WIN.fill(BACKGROUND_COLOUR)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]: #left
        yellow.x -= x_velocity
    if keys_pressed[pygame.K_d]: #right
        yellow.x += x_velocity
    if keys_pressed[pygame.K_w]: #up
        yellow.y -= y_velocity
    if keys_pressed[pygame.K_s]: #down
        yellow.y += y_velocity

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]: #left
        red.x -= x_velocity
    if keys_pressed[pygame.K_RIGHT]: #right
        red.x += x_velocity
    if keys_pressed[pygame.K_UP]: #up
        red.y -= y_velocity
    if keys_pressed[pygame.K_DOWN]: #down
        red.y += y_velocity



# Constructor
if __name__ == '__main__':
    main()

    