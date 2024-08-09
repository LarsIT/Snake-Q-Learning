# Snake the game
import pygame as pg

pg.init()

# Window
screen_size = 1000
TILE_SIZE = 25

SCREEN_HEIGHT = screen_size
SCREEN_WIDTH = screen_size
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("I want to die")

# Assertion: display and tile alignment
assert SCREEN_HEIGHT % TILE_SIZE == 0, "screen_size should be a multiple of TILE_SIZE"

# Clock
clock = pg.time.Clock()
FPS = 15

# Player scaled to display and tile size
scale = SCREEN_HEIGHT/(2*TILE_SIZE)
position_center = scale*TILE_SIZE
size = TILE_SIZE+1

player = pg.Rect((position_center, position_center, size, size))


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
    draw_grid(TILE_SIZE)

    # The Player
    pg.draw.rect(screen, (255, 0, 0), player)

    # Movement
    key = pg.key.get_pressed()
    if key[pg.K_a]:
        player.move_ip(-TILE_SIZE, 0)
    elif key[pg.K_d]:
        player.move_ip(TILE_SIZE, 0)
    elif key[pg.K_w]:
        player.move_ip(0, -TILE_SIZE)
    elif key[pg.K_s]:
        player.move_ip(0, TILE_SIZE)

    # Quit game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()

# Event handler
