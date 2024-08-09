# Snake the game
import pygame as pg
# TODO: assure the dimensions all align

pg.init()

# Window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pg.display.set_caption("I want to die")

# Clock
clock = pg.time.Clock()
FPS = 15

# Player
player = pg.Rect((250, 250, 50, 50))


# Grid
BACKGROUND_COLOR = (0, 0, 0)
LINE_COLOR = (200, 200, 200)


def draw_grid(tile_size):
    """Function to draw a grid for the game, the snake can only move according to the grid"""
    screen.fill(BACKGROUND_COLOR)

    # vertical lines
    for x in range(tile_size, SCREEN_WIDTH, tile_size):
        pg.draw.line(screen, LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT))

    # horizontal lines
    for y in range(tile_size, SCREEN_HEIGHT, tile_size):
        pg.draw.line(screen, LINE_COLOR, (0, y), (SCREEN_WIDTH, y))
    pass


# Loop
run = True
while run:
    # Frame rate
    clock.tick(FPS)

    # Screen refresh
    draw_grid(50)

    # The Player
    pg.draw.rect(screen, (255, 0, 0), player)

    # Movement
    key = pg.key.get_pressed()
    if key[pg.K_a]:
        player.move_ip(-50, 0)
    elif key[pg.K_d]:
        player.move_ip(50, 0)
    elif key[pg.K_w]:
        player.move_ip(0, -50)
    elif key[pg.K_s]:
        player.move_ip(0, 50)

    # Quit game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()

# Event handler
