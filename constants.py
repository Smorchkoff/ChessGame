import pygame
pygame.init()
info_rect_width = 200
info_rect_height = 100
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 8, 8
SQUARE_WIDTH = (WIDTH + 80) // ROWS
SQUARE_HEIGHT = (HEIGHT + 50) // COLS

piece_size = (75, 75)

WIN = pygame.display.set_mode((WIDTH + info_rect_width, HEIGHT + info_rect_height))

white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

BLACK = 'black'
BLACK_SQUARE = 'darkgray'
WHITE = 'lightgray'

