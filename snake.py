import pygame as pg
from random import randrange

# Constants for the game
WINDOW = 1000
TILE_SIZE = 50
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
FPS = 60
time, TIMESTEP = 0, 110

# Position randomizer
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]

# Control restriction dictionary
control_direction = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

# Snake instance
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_direction = (0, 0)

# Apple instance
apple = snake.copy()
apple.center = get_random_position()

# Game loop
while True:
    pg.display.flip()
    clock.tick(60)
    screen.fill("black")

    for event in pg.event.get():
        # Quit game
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            exit()
        # Control
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and control_direction[pg.K_w]:
                snake_direction = (0, -TILE_SIZE)
                control_direction = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            elif event.key == pg.K_s and control_direction[pg.K_s]:
                snake_direction = (0, TILE_SIZE)
                control_direction = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            elif event.key == pg.K_a and control_direction[pg.K_a]:
                snake_direction = (-TILE_SIZE, 0)
                control_direction = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            elif event.key == pg.K_d and control_direction[pg.K_d]:
                snake_direction = (TILE_SIZE, 0)
                control_direction = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}

    # Check collisions
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if any([snake.left < 0, snake.right > WINDOW, snake.top < 0, snake.bottom > WINDOW, self_eating]):
        snake.center, apple.center = get_random_position(), get_random_position()
        length, snake_direction = 1, (0, 0)
        segments = [snake.copy()]

    # Check apple
    if snake.center == apple.center:
        apple.center = get_random_position()
        length += 1

    # Draw apple
    pg.draw.rect(screen, "red", apple)

    # Draw snake
    [pg.draw.rect(screen, "green", segment) for segment in segments]
    # Move snake
    time_now = pg.time.get_ticks()
    if time_now - time > TIMESTEP:
        time = time_now
        snake.move_ip(snake_direction)
        segments.append(snake.copy())
        segments = segments[-length:]
