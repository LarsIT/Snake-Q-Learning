# Snake the game
from pprint import pprint

import pygame as pg

pg.init()

# Window
screen_size = 1000
TILE_SIZE = 50

SCREEN_HEIGHT = screen_size
SCREEN_WIDTH = screen_size
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Kill me")

# Assertion: display and tile alignment
assert SCREEN_HEIGHT % TILE_SIZE == 0, "screen_size should be a multiple of TILE_SIZE"

# Clock for frame rate and game speed
clock = pg.time.Clock()
FPS = 10

# Grid
BACKGROUND_COLOR = (0, 0, 0)
LINE_COLOR = (200, 200, 200)
SNAKE_COLOR = (50, 200, 50)


def draw_grid(tile_size):
    """Function to draw a grid for the game, the snake can only move according to the grid"""
    screen.fill(BACKGROUND_COLOR)

    # vertical lines
    for x in range(tile_size, SCREEN_WIDTH, tile_size):
        pg.draw.line(screen, LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT))

    # horizontal lines
    for y in range(tile_size, SCREEN_HEIGHT, tile_size):
        pg.draw.line(screen, LINE_COLOR, (0, y), (SCREEN_WIDTH, y))


class Snake:
    """Snake class"""

    def __init__(self, x, y, color):
        # Position and image of snake
        self.x = x
        self.y = y
        self.color = color
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        # Default attributes for movement of snake
        self.moving = False
        self.velocity = 1
        self.dx = self.velocity
        self.dy = 0

    def position(self):
        """Snake's position"""
        return self.x, self.y

    def move(self):
        """Snake's movement"""
        if self.moving:
            self.x += self.dx
            self.y += self.dy

    def control(self):
        """Control snake's direction based on key press"""
        key = pg.key.get_pressed()

        # Snake starts when any key is pressed
        if any(key):
            self.moving = True

        if key[pg.K_a]:
            self.dx = -self.velocity
            self.dy = 0
        elif key[pg.K_d]:
            self.dx = self.velocity
            self.dy = 0
        elif key[pg.K_w]:
            self.dx = 0
            self.dy = -self.velocity
        elif key[pg.K_s]:
            self.dx = 0
            self.dy = self.velocity

    def update(self):
        """Update snake's position on screen"""
        # Fill snake
        self.image.fill(self.color)

        # Snake position (inside tiles)
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE

        # Draw snake
        screen.blit(self.image, self.rect)


snake = Snake(0, 0, SNAKE_COLOR)


def collision(x, y) -> None:
    global run
    number_tiles = screen_size / TILE_SIZE
    if any([x >= number_tiles,
            x < 0,
            y >= number_tiles,
            y < 0]):
        run = False


# Loop
run = True
while run:
    # Frame rate
    clock.tick(FPS)

    # Screen refresh
    draw_grid(TILE_SIZE)

    # The Player
    snake.control()
    snake.move()
    snake.update()
    collision(snake.position()[0], snake.position()[1])

    # Event handler
    for event in pg.event.get():
        # Quit game
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            run = False

    pg.display.update()

pg.quit()


